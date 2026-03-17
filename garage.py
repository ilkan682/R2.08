from obj_voitures import Voitures

# Création des voitures
captur = Voitures("Renault", "Captur_TCE_90ch", 2022, 20000, "Gris foncé", 7.2)
clio = Voitures("Renault", "Clio_TCE_100ch", 2018, 17000, "Bleu nuit", 5.5)

# Distance Colmar → Biarritz
distance = 1060

# Calcul CO2 pour chaque voiture
co2_clio = clio.calcul_co2(distance)
co2_captur = captur.calcul_co2(distance)

print(f"CO2 émis Clio : {co2_clio:.2f} kg pour {distance} km")
print(f"CO2 émis Captur : {co2_captur:.2f} kg pour {distance} km")

# Comparaison approximative TGV : 3,9 kg / passager
co2_tgv = 3.9 * 1  # 1 passager
print(f"CO2 émis par TGV sur {distance} km : {co2_tgv:.2f} kg par passager")