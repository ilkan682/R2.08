class Voitures:
    # Attribut de classe
    prix_litre = 1.70  # €/L

    def __init__(self, marque="Ferrari", modele="SF90_spider", annee=2010,
                 prix=None, couleur="Blanc", conso=6.0):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
        self.couleur = couleur
        self.conso = conso  # litres / 100 km

    def __str__(self):
        return (f"{self.marque} {self.modele} {self.annee} | "
                f"Prix: {self.prix} € | Couleur: {self.couleur} | "
                f"Conso: {self.conso} L/100km")

    # Méthodes existantes
    def calcul_consommation(self, distance):
        return (distance * self.conso) / 100

    def calcul_prix(self, distance):
        litres = self.calcul_consommation(distance)
        return litres * Voitures.prix_litre

    def modif_prix_litre(self, nouveau_prix):
        Voitures.prix_litre = nouveau_prix

    # Nouvelle méthode calcul CO2
    def calcul_co2(self, distance):
        """Retourne le CO2 émis en kg pour la distance donnée"""
        litres = self.calcul_consommation(distance)
        return litres * 2.3  # 2,3 kg CO2 par litre d’essence