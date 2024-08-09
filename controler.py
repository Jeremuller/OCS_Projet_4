from views import TournamentView
from models import Tournament, Player


class TournamentController:

    def __init__(self):
        self.view = TournamentView()
        self.tournament = None

    def start(self):

        TournamentView.display_welcome_message()

        while True:
            main_menu_choice = TournamentView.display_menu()

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

    def tournament_in_progress(self):
        return self.tournament is not None

    def create_tournament(self):
        if self.tournament_in_progress():
            print("Un tournoi est déjà en cours. Veuillez le terminer ou l'annuler d'abord.")

        name, location, date, description = TournamentView.get_tournament_informations()
        self.tournament = Tournament(name, location, date, description)
        TournamentView.display_tournament_infos(self.tournament)

    def add_player(self):
        if self.tournament_in_progress():
            family_name, first_name, date_of_birth = TournamentView.get_player_informations()
            player = Player(family_name, first_name, date_of_birth)
            self.tournament.add_player(player)
            TournamentView.display_players(self.tournament.players_list)
        else:
            print("Il n'y a pas de tournoi en cours")

    def start_tournament(self):
        if self.tournament_in_progress():
            if not self.tournament.players_list:
                print("Le tournoi n'a aucun joueur!")
                return
            turn = self.tournament.create_turn(f"round_{self.tournament.actual_turn_number + 1}")
            matches = turn.generate_matches()
            TournamentView.display_match_results(matches)

    def informations_menu(self):
        while True:
            informations_menu_choice = TournamentView.display_menu()

            if informations_menu_choice == "1":
                if self.tournament_in_progress():
                    TournamentView.display_tournament_infos(self.tournament)
                else:
                    print("Il n'y a aucun tournoi en cours.")
            elif informations_menu_choice == "2":
                if self.tournament_in_progress():
                    TournamentView.display_players(self.tournament)
                else:
                    print("Il n'y a aucun tournoi en cours.")
            elif informations_menu_choice == "3":
                if self.tournament_in_progress():
                    TournamentView.display_tournament_turns(self.tournament)
                else:
                    print("Il n'y a aucun tournoi en cours.")
            elif informations_menu_choice == "4":
                print("cette partie est en cours de développement")
                pass
                # ajouter une liaison vers les joueurs enregistrés
            elif informations_menu_choice == "5":
                print("cette partie est en cours de développement")
                pass
                # ajouter une liaison vers les tournois archivés
            elif informations_menu_choice == "6":
                break
            else:
                print("Choix invalide, veuillez entre le chiffre correspondant à votre requête")


# Point d'entrée du programme
if __name__ == "__main__":
    controller = TournamentController()
    controller.start()
