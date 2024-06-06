import math

# Données du village
consommation_moyenne_habitant = 2223000
habitants = 2000
consommation_village = consommation_moyenne_habitant * habitants

# Eolienne
coefficient_eolien = 1.0
fonctionnement_eolien = 0.5
prix_une = 70000
puissance_une = 20000
energie_une = puissance_une * 365.25 * 24 * fonctionnement_eolien
nombre_eolienne = math.ceil(consommation_village / energie_une)
prix_total = nombre_eolienne * prix_une
print("Prix total si 100% éolien :", prix_total, "=", prix_total / 1000000, "millions d'euros")

# Solaire
