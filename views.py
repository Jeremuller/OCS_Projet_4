from models import Player, Tournament, Turn, Match, tournoi_test


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
        print("Veuillez entrer le chiffre correspondant à votre requête")

    @staticmethod
    def display_informations_menu():
        print("\nAfficher informations:")
        print("1. Afficher les informations du tournoi")
        print("2. Afficher les joueurs participants au tournoi")
        print("3. Afficher les tours du tournoi et leurs matchs")
        print("4. Afficher les joueurs enregistrés")
        print("5. Afficher les autres tournois enregistrés")
        print("6. Retour au menu principal")
        print("Veuillez entrer le chiffre correspondant à votre requête")

    @staticmethod
    def display_tournament_infos(tournament):
        print(f"\nDétails du tournoi {tournament.name}:")
        print(f"Date: {tournament.date}")

    @staticmethod
    def display_players(tournament):
        tournament.players_list.sort(key=lambda player: (player.family_name, player.first_name))
        print("\nListe des joueurs:")
        for player in tournament.players_list:
            print(f"{player.family_name} {player.first_name}")

    @staticmethod
    def display_tournament_turns(tournament):
        print(f"\n Tours du tournoi {tournament.name}:")
        for turn in tournament.turns_list:
            print(turn.name)
            for turn.match in turn.matches:
                print(str(turn.match))


TournamentView.display_tournament_turns(tournoi_test)
TournamentView.display_tournament_infos(tournoi_test)
TournamentView.display_welcome_message()
TournamentView.display_menu()


