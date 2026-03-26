def menu_ajouter_auteur(self):
    print(f"\n{Ihm.CYAN}--- AJOUTER UN AUTEUR ---{Ihm.NO_COLOR}")
    nom = input("Nom de l'auteur ? : ")
    prenom = input("Prénom de l'auteur ? : ")
    pays = input("Pays d'origine ? : ")
    date_n = input("Date de naissance (JJ/MM/AAAA) ? : ")
    nouvel_auteur = Auteur(nom, prenom, pays, date_n)
    self.biblio.auteurs.append(nouvel_auteur)
    print(f"\t{Ihm.VERT}----> L'auteur {nouvel_auteur.prenom} {nouvel_auteur.nom} a été ajouté.{Ihm.NO_COLOR}")
    input("Appuyer sur Entrée pour continuer...")
    self.choix = 0


def menu_ajouter_livre(self):
    self.menu_lister_auteurs()
    print(f"\n{Ihm.CYAN}--- AJOUTER UN LIVRE ---{Ihm.NO_COLOR}")
    self.__attendre_choix_ligne(range(1, len(self.biblio.auteurs) + 1), "--> Choisissez un auteur (numéro) : ")
    auteur = self.biblio.auteurs[self.choix - 1]
    titre = input("--> Entrez le titre du livre ? : ")
    isbn = input("--> Son numéro ISBN ? : ")
    annee = input("--> Année de publication ? : ")
    nouveau_livre = Livre(titre, auteur, isbn, annee)
    self.biblio.livres.append(nouveau_livre)
    print(f"\t{Ihm.VERT}----> Le livre '{titre}' a été ajouté.{Ihm.NO_COLOR}")
    input("Appuyer sur Entrée pour continuer...")
    self.choix = 0


def menu_supprimer_livre(self):
    self.menu_lister_livres()
    print(f"\n{Ihm.CYAN}--- SUPPRIMER UN LIVRE ---{Ihm.NO_COLOR}")
    self.__attendre_choix_ligne(range(1, len(self.biblio.livres) + 1),
                                "--> Choisissez le livre à supprimer (numéro) : ")
    livre = self.biblio.livres[self.choix - 1]
    confirm = input(f"Veuillez confirmer la suppression de '{livre.titre}' (OUI) : ")
    if confirm == "OUI":
        self.biblio.livres.remove(livre)
        print(f"\t{Ihm.VERT}----> Le livre a été supprimé.{Ihm.NO_COLOR}")
    input("Appuyer sur Entrée pour continuer...")
    self.choix = 0