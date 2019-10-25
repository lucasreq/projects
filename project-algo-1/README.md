# Projet de calcul routier

## contexte
Le but de ce projet est de construire un programme qui va calculer le temps de livraison d'une commande entre une ville et une autre en respectant quelques indications.

Indication : 
- Un camion accélère de 10km/h, par minute.
- Un camion ralenti de 10km/h, par minute.
- Sa vitesse maximale est de 90 km/h.
- Un conducteur doit faire une pause de 15 min toutes les 2 heures.

Mon programme utilise le langage Python et utilise une base de donnée en json.

librairies utilisés :
- math 
- json

## utilisation

- lancez le programme
- entrez la ville de départ et la ville d'arrivée (Attention les villes comme paris ou marseille on besoin d'un numéro d'arrondissement ex: paris 01 )
- le programme va ensuite sortir un tableau de : 
ville de départ : ville1   | ville d'arrivée :   ville2  | distance parcouru en km | heure : minutes | nombre de pauses