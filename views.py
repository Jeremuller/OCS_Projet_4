from models import Player, Turn


class TournamentView:

    @staticmethod
    def display_welcome_message():
        print("Bienvenue au tournoi d'échecs!")

    @staticmethod
    def display_menu():
        print("\nMenu principal:")
        print("1. Créer un nouveau tournoi")
        print("2. Ajouter un joueur")
        print("3. Démarrer le tournoi")
        print("4. Afficher informations")
        print("5. Quitter")
        main_menu_choice = input("Veuillez entrer le chiffre correspondant à votre requête: ")
        return main_menu_choice

    @staticmethod
    def display_informations_menu():
        print("\nAfficher informations:")
        print("1. Afficher les informations du tournoi")
        print("2. Afficher les joueurs participants au tournoi")
        print("3. Afficher les tours du tournoi et leurs matchs")
        print("4. Afficher les joueurs enregistrés")
        print("5. Afficher les autres tournois enregistrés")
        print("6. Retour au menu principal")
        informations_menu_choice = input("Veuillez entrer le chiffre correspondant à votre requête: ")
        return informations_menu_choice

    # Gestion des données
    @staticmethod
    def load_players_data():
        players_data = Player.deserialisation_from_dict("players_list.json")
        return players_data

    @staticmethod
    def load_turns_data():
        turns_data = Turn.serialisation_to_dict("turns_list.json")
        return turns_data

    @staticmethod
    def display_tournament_infos(tournament):
        print(f"\nDétails du tournoi {tournament.name}:")
        print(f"Date: {tournament.date}")

    @staticmethod
    def display_players(players_list):
        players_list.sort(key=lambda player: (player.family_name, player.first_name))
        print("\nListe des joueurs:")
        for player in players_list:
            print(f"{player.family_name} {player.first_name}")

    @staticmethod
    def display_tournament_turns(tournament):
        print(f"\n Tours du tournoi {tournament.name}:")
        for turn in tournament.turns_list:
            print(turn.name)
            for turn.match in turn.matches:
                print(str(turn.match))

    @staticmethod
    def display_match_results(matches):
        print("\nRésultats des matchs: ")
        for match in matches:
            print(f"{match.player1} vs {match.player2} ->> vainqueur: {match.result}")

    @staticmethod
    def get_player_informations():
        print("Veuillez entrer les informations du joueurs que vous souhaitez inscrire")
        family_name = input("Nom: ")
        first_name = input("Prénom: ")
        date_of_birth = input("Date de naissance (format JJMMAAAA): ")
        return family_name, first_name, date_of_birth

    @staticmethod
    def get_tournament_informations():
        print("Veuillez entrer les informations du tournoi à créer")
        name = input("Nom: ")
        location = input("Lieu: ")
        date = input("Date (format JJMMAAAA) : ")
        description = input("Description: ")
        return name, location, date, description

    @staticmethod
    def get_match_results(match):
        while True:
            print(f"Match: {match.player1.family_name} {match.player1.first_name} vs "
                  f"{match.player2.family_name} {match.player2.first_name}")
            result = input(f"Le joueur {match.player1.family_name} {match.player1.first_name} "
                           f"a t'il gagné? (oui/non/draw en cas d'égalité): ").lower()

            if result == "oui":
                return 1, 0
            elif result == "non":
                return 0, 1
            elif result == "draw":
                return 0.5, 0.5
            else:
                print("Résultat invalide, veuillez entrer le nom du gagnant, ou \"draw\" en cas d'égalité")
