# ==========================================
# PARTIE 1 : La classe PARENT
# ==========================================
class Animal:
    def __init__(self, nom, age, **kwargs):
        # Initialisation des attributs de la classe Animal
        self.nom = nom
        self.age = age
        # Propagation aux classes suivantes dans le MRO
        super().__init__(**kwargs)

    def se_presenter(self):
        # On appelle le super() d'abord pour afficher le Personnage avant l'Animal
        if hasattr(super(), 'se_presenter'):
            super().se_presenter()
        # Affichage avec DEUX tabulations comme demandé
        print(f"\t\tJe me nomme {self.nom}, j'ai {self.age} ans")

# ==========================================
# PARTIE 2 : La classe ENFANT (Mammifere)
# ==========================================
class Mammifere(Animal):
    def __init__(self, nom, age, race, type_pelage, couleur, **kwargs):
        # Initialisation des attributs propres à Mammifere
        self.race = race
        self.type_pelage = type_pelage
        self.couleur = couleur
        # Appel à super() pour construire nom et age (et propager la suite)
        super().__init__(nom=nom, age=age, **kwargs)

    def se_presenter(self):
        print(f"Je suis un(e) {self.race} revêtu de {self.type_pelage} de couleur: {self.couleur}.")
        # Appel de la méthode jumelle
        super().se_presenter()

# ==========================================
# PARTIE 3 : Une seconde classe ENFANT (Oiseau)
# ==========================================
class Oiseau(Animal):
    def __init__(self, nom, age, ordre, envergure, **kwargs):
        # Initialisation des attributs propres à Oiseau
        self.ordre = ordre
        self.envergure = envergure
        # Appel à super() pour construire nom et age
        super().__init__(nom=nom, age=age, **kwargs)

    def se_presenter(self):
        print(f"Je suis un oiseau de type {self.ordre} et mon envergure est de {self.envergure} cm.")
        # Appel de la méthode jumelle
        super().se_presenter()

# ==========================================
# ACTIVITÉ COMPLÉMENTAIRE : Héritage Multiple
# ==========================================
class Personnage:
    def __init__(self, style, titre, **kwargs):
        self.style = style
        self.titre = titre
        super().__init__(**kwargs)

    def se_presenter(self):
        # Affichage avec UN tab
        print(f"\tJe joue dans le {self.style}: {self.titre}")
        if hasattr(super(), 'se_presenter'):
            super().se_presenter()

class ActeurMammifere(Mammifere, Personnage):
    def __init__(self, nom, age, race, type_pelage, couleur, style, titre):
        # Mise en oeuvre unique de la fonction super()
        super().__init__(nom=nom, age=age, race=race, type_pelage=type_pelage, couleur=couleur, style=style, titre=titre)

class ActeurOiseau(Oiseau, Personnage):
    def __init__(self, nom, age, ordre, envergure, style, titre):
        # Mise en oeuvre unique de la fonction super()
        super().__init__(nom=nom, age=age, ordre=ordre, envergure=envergure, style=style, titre=titre)

# ==========================================
# PROGRAMME PRINCIPAL (Tests)
# ==========================================
if __name__ == "__main__":
    animaux = [
        ActeurMammifere("Simba", 5, "lion", "poils courts", "fauve clair", "dessin animé", "Le livre de la jungle"),
        ActeurMammifere("Beethoven", 3, "chien", "poils longs", "blanche & fauve", "film", "Beethoven"),
        ActeurMammifere("César", 26, "singe", "poils courts", "marron", "film", "La planète des singes"),
        ActeurMammifere("Dumbo", 1, "éléphanteau", "peau nue", "grise", "dessin animé", "Dumbo"),
        ActeurOiseau("Hedwige", 7, "rapace", 90, "film", "Harry Potter"),
        ActeurOiseau("Blu", 5, "perroquet", 100, "dessin animé", "Rio"),
        ActeurOiseau("Lago", 12, "perroquet", 60, "film", "Aladin"),
        ActeurOiseau("Zazu", 40, "passereau", 0, "dessin animé", "Le roi lion")
    ]

    print(f"MRO de ActeurMammifere: {ActeurMammifere.mro()}")
    print(f"MRO de ActeurOiseau: {ActeurOiseau.mro()}\n")

    for animal in animaux:
        animal.se_presenter()
        print() # Ligne vide pour séparer chaque animal