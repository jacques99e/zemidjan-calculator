

#  Calculateur de Trajet Zemidjan/Taxi - Lomé

Un programme Python qui calcule le prix d'un trajet en zemidjan (moto-taxi) ou taxi (voiture) à Lomé, en tenant compte des tarifs de base, du prix au kilomètre et des majorations aux heures de pointe.

##  Fonctionnalités

-  Choix entre zemidjan et taxi
-  Calcul automatique selon la distance
-  Détection des heures de pointe (matin, midi, soir)
-  Majoration automatique (+15% zem, +25% taxi)
-  Historique des trajets pendant la session
-  Gestion des erreurs de saisie
-  Possibilité de calculer plusieurs trajets à la suite

##  Comment lancer le programme

Prérequis
- Python 3.6 ou supérieur installé sur votre ordinateur
- Aucune bibliothèque externe nécessaire (Python pur)

### Installation et exécution

1. Clonez ce dépôt ou téléchargez les fichiers :
```bash
git clone https://github.com/jacques99e/zemidjan-calculator.git
cd zemidjan-calculator 

# Lancez le programme :

python main.py

# Exemple d'utilisation

==================================================
  CALCULATEUR DE TRAJET - LOMÉ 
==================================================

Bienvenue ! Ce programme calcule le prix de votre trajet
en zemidjan (moto-taxi) ou taxi (voiture) à Lomé.

--------------------------------------------------
CHOIX DU TRANSPORT :
1. Zemidjan (moto-taxi)
2. Taxi (voiture)
3. Afficher l'historique
4. Quitter le programme
--------------------------------------------------
Votre choix (1, 2, 3 ou 4) : 1
Distance du trajet (en km) : 5
À quelle heure part le trajet ? (format HH:MM, ex: 07:30) : 07:30

==================================================
RÉCAPITULATIF DU TRAJET 
==================================================
Transport : Zemidjan (moto-taxi)
Distance : 5.0 km
Heure : 07h30
--------------------------------------------------
Tarif de base : 150 FCFA
Prix au km : 75 FCFA/km
Sous-total : 525.00 FCFA
Heure de pointe détectée !
Majoration appliquée : 15%
==================================================
PRIX TOTAL : 603.75 FCFA
==================================================

# Tarifs

Transport	Tarif de base	Prix/km	Majoration heure de pointe
Zemidjan	150 FCFA	75 FCFA	+15%
Taxi	200 FCFA	100 FCFA	+25%

# Heures de pointe

Matin : 07h00 - 08h45

Midi : 11h45 - 13h00
Soir : 17h00 - 19h00

# Structure du code

Le programme est organisé en plusieurs fonctions :

est_heure_pointe(heure) : Vérifie si une heure est en période de pointe

demander_heure() : Demande et valide l'heure saisie par l'utilisateur

calculer_prix_trajet(transport, distance, heure) : Calcule le prix total

afficher_resultat(details) : Affiche un récapitulatif formaté

main() : Programme principal avec la boucle de menu

# Contexte

ce projet a été réalisé dans le cadre du challenge 30 Days of Python 2026 organisé par Python Software Community Togo en partenariat avec Fata, en préparation de la PyCon Togo 2026.

# Auteur

NOUSSOUGAN Edoh Jacques
GitHub : jacques99e
Challenge : 30 Days of Python 2026

# Licence

Ce projet est un exercice d'apprentissage personne