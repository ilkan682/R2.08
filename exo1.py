class Voitures():
    def __init__(self, marque="ferrari", modele="SF90_spider", annee=2010) :

        self.marque = marque
        self.annee = annee
        self.modele = modele

    def __str__(self):
        # Redéfinition pour le print(instance)...
        return f"Valeurs des attributs de l’instance : {self.marque} {self.modele} {self.annee}"




car = Voitures("Renault", "Clio", 2018) # Création d’une instance.
car2 = Voitures("citroen ", "ds5", 2012)
voiture = Voitures("citroen  ", "c3")
caisse = car.modele # Lecture d’un attribut d’instance.
print(f"J’ai une {car.marque} {caisse} de {car.annee} !") # Affichage.
car.annee = 2020 # Ecriture (modification) d’un attribut d’instance.
print(f"J’ai une {car.marque} {caisse} de {car.annee} !")

print(car2)
print(voiture)

voiture4 = Voitures()
print(voiture4)

voiture5 = Voitures("F40")
print(voiture5)


voiture6 = Voitures(modele="296_GTS")
print(voiture6)


print(type(voiture6))
print(voiture6.__class__)


print(vars(voiture6))
print(voiture6.__dict__)


print(dir(voiture6))