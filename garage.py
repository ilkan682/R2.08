from obj_voitures import Voitures

# Création d’une voiture
clio = Voitures("Renault", "Clio_TCE_100ch", 2018, 17000, "Bleu nuit", 5.5)

# 33. Affichage direct des attributs (protégé et privé)
print(clio._id_serie)       # None
print(clio._Voitures__audio_code)  # None (nom mangling pour privé)

# 34. Appel de la méthode d'affichage
clio.affiche_prot_priv()  # ID Série : None | Audio Code : None

# 35. Test des setters et getters
print("Set id_serie :", clio.set_id_serie("AB1234"))       # True
print("Set audio_code :", clio.set_audio_code("1234"))     # True
print("Set audio_code invalide :", clio.set_audio_code("12AB"))  # False

# Affichage via getters
print("ID série :", clio.get_id_serie())       # AB1234
print("Audio code :", clio.get_audio_code())   # 1234

# Affichage via méthode dédiée
clio.affiche_prot_priv()  # ID Série : AB1234 | Audio Code : 1234