""" Calculateur de Trajet Zemidjan/Taxi - Lomé
Projet Final - 30 Days of Python Challenge 2026
Python Software Community Togo
"""

def est_heure_pointe(heure):
    """"Vérifie si une heure donnée est dans une plage d'heure de pointe.
    Args:
        heure: Un nombre à virgule (ex: 7.5 pour 7h30)
    Returns:
        True si c'est l'heure de pointe, False sinon
    """
    debut_matin = 7.0
    fin_matin = 8.75
    debut_midi = 11.75
    fin_midi = 13.5
    debut_soir = 17
    fin_soir = 19
    if debut_matin <= heure <= fin_matin:
        return True
    elif debut_midi <= heure <= fin_midi:
        return True
    elif debut_soir <= heure <= fin_soir:
        return True
    else:
        return False
def demender_heure():
    """Demande l'heure du trajet à l'utilisateur et la convertit en décimal.
    Returns:
        L'heure en notation décimale (ex: 7.5 pour 7h30)
    """
    while True:
        try:
            saisie = input("Entrez l'heure du trajet (format HH:MM, ex: 7:30): ")
            heures_str, minutes_str = saisie.split(":")
            heures = int(heures_str)
            minutes = int(minutes_str)
            if heures < 0 or heures > 23 or minutes < 0 or minutes > 59:
                print("Heure invalide. Veuillez entrer une heure entre 00:00 et 23:59.")
                continue
            return heures + (minutes / 60)
        except ValueError:
            print("Format invalide. Veuillez entrer l'heure au format HH:MM.")
        except Exception:
            print("Une erreur est survenue. Veuillez réessayer.")
def calculer_prix_trajet(transport, distance, heure):
    """Calcule le prix total d'un trajet.
    Args:
        transport: Type de transport ('zemidjan' ou 'taxi')
        distance: Distance du trajet en kilomètres
        heure: Heure du trajet en notation décimale
    Returns:
        dictionnaire contenant les détails du calcul
    """
    if transport == "zemidjan":
        tarif_base = 150
        prix_km = 75
        majoration_pourcentage = 15
        nom_transport = "zemidjan(moto-taxi)"
    elif transport == "taxi":
        tarif_base = 200
        prix_km = 100
        majoration_pourcentage = 25
        nom_transport = "taxi(voiture)"
    else:
        raise ValueError("Transport invalide")
    prix_base = tarif_base + (prix_km * distance)
    en_heure_pointe = est_heure_pointe(heure)
    if en_heure_pointe:
        prix_final = prix_base * (1 + majoration_pourcentage / 100)
    else:
        prix_final = prix_base
    return {
        "transport": nom_transport,
        "distance": distance,
        "heure": heure,
        "tarif_base": tarif_base,
        "prix_km": prix_km,
        "prix_base": prix_base,
        "en_heure_pointe": en_heure_pointe,
        "majoration_pourcentage": f"{majoration_pourcentage}%",
        "prix_final": prix_final
    }
def afficher_resultats(details):
    """Affiche un joli récapitulatif du trajet.
    Args:
        details: Le dictionnaire retourné par calculer_prix_trajet
    """
    print()
    print("="*50)
    print("RECAPITULATIF DU TRAJET")
    print("="*50)
    print(f"Transport : {details['transport']}")
    print(f"Distance : {details['distance']}km")
    heures = int(details['heure'])
    minutes = int((details['heure'] - heures) * 60)
    print(f"Heure : {heures:02d}h{minutes:02d}")
    print("-" * 50)
    print(f"Tarif de bbase : {details['tarif_base']} FCFA")
    print(f"Prix au km : {details['prix_km']} FCFA/km")
    print(f"Sous-total : {details['prix_base']:.2f} FCFA")
    if details['en_heure_pointe']:
        print("Heure de pointe détectée!")
        print(f"Majoration appliquée : {details['majoration_pourcentage']}")
    else:
        print("Tarif normal (hors heure de pointe)")
    print("=" * 50)
    print(f"PRIX TOTAL : {details['prix_final']:.2f} FCFA")
    print("=" * 50)
    print()
def main():
    """
    Programme principal qui gère la boucle de calculs multiples.
    """
    print()
    print("=" * 50)
    print("CALCULATEUR DE TRAJET - LOME")
    print()
    print("Bienvenue ! Ce programme calcule le prix de votre trajet")
    print("en zemidjan (moto-taxi) ou taxi (voiture) à lomé.")
    print()
    # Historique des trajets
    historique = []
    nombre_trajets = 0
    while True:
        # --- CHOIX DU TRANSPORT ---
        print('-' * 50)
        print("CHOIX DU TRANSPORT :")
        print("1. Zemidjan (moto-taxi)")
        print("2. Taxi (voiture)")
        print("3. Afficher l'historique")
        print("4. Quitter le programme")
        print("-" *50)
        choix = input("Votre choix (1, 2, 3 ou 4)").strip()
        # Gestion des choix 3 et 4
        if choix == "3":
            if len(historique) == 0:
                print("\n Aucun trajet dans l'historique pour le moment.")
            else:
                print("\n HISTORIQUE DES TRAJETS :")
                for i, trajet in enumerate(historique, 1):
                    h = int(trajet['heure'])
                    m = int((trajet['heure'] - h) * 60)
                    print(f" {i}. {trajet['transport']} - {trajet['distance']}km "
                          f"à {h:02d}h{m:02d}m\n {trajet['prix_final']:.2f} FCFA")
            print()
            continue
        if choix == "4":
            print(f"\n Merci d'avoir utilisé le calculateur !")
            print(f"Vous avec calculé {nombre_trajets} trajet(s) au total.")
            print("A bientôt!")
            break
        if choix == "1":
            transport = "zemidjan"
        elif choix == "2":
            transport = "taxi"
        else:
            print("Choix invalide. Veuillez sélectionner 1, 2, 3 ou 4.")
            continue
        while True:
            try:
                distance = float(input("Distance du trajet (en km) :"))
                if distance <= 0:
                    print("La distance doit être supérieure à 0 km.")
                    continue
                break
            except ValueError:
                print("Veuillez entrer un nombre valide (ex: 5.5 pour 5,5 km)")
        # --- HEURE ---
        heure = demender_heure()
        # --- CALCUL ---
        resultat = calculer_prix_trajet(transport, distance, heure)
        # --- AFFICHAGE ---
        afficher_resultats(resultat)
        # --- SAUVEGARDE DANS L'HISTORIQUE ---
        historique.append(resultat)
        nombre_trajets += 1
        # --- DEMANDER SI ON CONTINUE ---
        continuer = input("Voulez-vous calculer un autre trajet ? (oui/non):")
        if continuer.lower() not in ["oui", "o", "yes", "y", "ok"]:
            print(f"\n Merci d'avoir utilisé le calculateur!")
            print(f"Vous avez calculé {nombre_trajets} trajet(s) au total.")
            print("A bientôt!")
            break
# Point d'entrée du programme
if __name__ == "__main__":
    main()