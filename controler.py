import views
from views import TournamentView
from models import Tournament, Player


class TournamentController:

    def __init__(self):
        self.view = TournamentView()
        self.tournament = None

    def start(self):

        TournamentView.display_welcome_message()
        main_menu_choice = TournamentView.display_menu()

        while True:

            if main_menu_choice == "1":
                self.create_tournament()
            elif main_menu_choice == "2":
                self.add_player()
            elif main_menu_choice == "3":
                self.start_tournament()
            elif main_menu_choice == "4":
                TournamentView.display_informations_menu()
            elif main_menu_choice == "5":
                print("Au revoir!")
                break
            else:
                print("Choix invalide, veuillez entre le chiffre correspondant à votre requête")

    def create_tournament(self):
        name, location, date, description = TournamentView.get_tournament_informations()
        self.tournament = Tournament(name, location, date, description)
        TournamentView.display_tournament_infos(self.tournament)

    def add_player(self):
        family_name, first_name, date_of_birth = TournamentView.get_player_informations()
        player = Player(family_name, first_name, date_of_birth)
        self.tournament.add_player(player)
        TournamentView.display_players(self.tournament.players_list)

    def start_tournament(self):
        if not self.tournament.players_list:
            print("Le tournoi n'a aucun joueur!")
            return
        turn = self.tournament.create_turn(f"round_{self.tournament.actual_turn_number + 1}")
        matches = turn.generate_matches()
        TournamentView.display_match_results(matches)

    def display_results(self):
        TournamentView.display_tournament_infos(self.tournament)
        TournamentView.display_players(self.tournament.players_list)


# Point d'entrée du programme
if __name__ == "__main__":
    controller = TournamentController()
    controller.start()
