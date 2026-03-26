from mediatheque import Bibliotheque, Ihm

if __name__ == "__main__":
    biblio = Bibliotheque("Auteurs.json", "Livres.json", "Membres.json")
    biblio.charger_auteurs(True)
    biblio.charger_livres(True)
    biblio.charger_membres(True)
    ihm = Ihm(biblio)
    while True:
        if ihm.choix == 0: ihm.menu_accueil()
        elif ihm.choix == 1: ihm.menu_lister_auteurs()
        elif ihm.choix == 2: ihm.menu_lister_livres()
        elif ihm.choix == 3: ihm.menu_lister_membres()
        # ... autres menus ...
        elif ihm.choix == 12: break # Quitter