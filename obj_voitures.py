import re

class Voitures:
    """
    Classe représentant un véhicule avec ses caractéristiques,
    méthodes de calcul de consommation, prix carburant et CO2.
    """

    # Attribut de classe
    prix_litre = 1.70  # €/L
    co2_par_litre = 2.3 # kg CO2 par litre d’essence

    def __init__(self, marque="Ferrari", modele="SF90_spider", annee=2010,
                 prix=None, couleur="Blanc", conso=6.0):
        """
        Constructeur de la classe Voitures
        """
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix
        self.couleur = couleur
        self.conso = conso  # litres / 100 km

        # Nouveaux attributs protégés / privés
        self._id_serie = None       # attribut protégé
        self.__audio_code = None    # attribut privé

    def __str__(self):
        """
        Affichage des informations principales du véhicule
        """
        return (f"{self.marque} {self.modele} {self.annee} | "
                f"Prix: {self.prix} € | Couleur: {self.couleur} | "
                f"Conso: {self.conso} L/100km")

    # ---------------- Méthodes existantes ----------------
    def calcul_consommation(self, distance):
        """Retourne la consommation en litres pour une distance donnée (km)"""
        return (distance * self.conso) / 100

    def calcul_prix(self, distance):
        """Retourne le prix du carburant pour une distance donnée"""
        litres = self.calcul_consommation(distance)
        return litres * Voitures.prix_litre

    def calcul_co2(self, distance):
        """Retourne la quantité de CO2 émise en kg pour une distance donnée"""
        litres = self.calcul_consommation(distance)
        return litres * Voitures.co2_par_litre

    def modif_prix_litre(self, nouveau_prix):
        """Modifie le prix du litre de carburant (attribut de classe)"""
        Voitures.prix_litre = nouveau_prix

    # ---------------- Nouvelle méthode ----------------
    def affiche_prot_priv(self):
        """Affiche les attributs protégés et privés"""
        audio_dechiffre = self.__decode_audio() if self.__audio_code else None
        print(f"ID Série : {self._id_serie} | Audio Code : {audio_dechiffre}")

    # ---------------- Getters / Setters ----------------
    # id_serie
    def get_id_serie(self):
        """Retourne l'ID série"""
        return self._id_serie

    def set_id_serie(self, num_serie):
        """Met à jour l'ID série si le format est correct (alphanumérique 6 à 12 caractères)"""
        if isinstance(num_serie, str) and re.fullmatch(r'[A-Za-z0-9]{6,12}', num_serie):
            self._id_serie = num_serie
            return True
        return False

    # audio_code
    def get_audio_code(self):
        """Retourne le code audio déchiffré"""
        return self.__decode_audio() if self.__audio_code else None

    def set_audio_code(self, code):
        """Encode et met à jour le code audio si le format est correct (4 chiffres)"""
        if isinstance(code, str) and re.fullmatch(r'\d{4}', code):
            self.__audio_code = self.__encode_audio(code)
            return True
        return False

    # ---------------- Méthodes internes pour le chiffrement ----------------
    def __encode_audio(self, code):
        """Chiffrement simple : renversement de la chaîne"""
        return code[::-1]

    def __decode_audio(self):
        """Déchiffre le code audio"""
        return self.__audio_code[::-1] if self.__audio_code else None
