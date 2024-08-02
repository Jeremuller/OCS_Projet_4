from views import TournamentView
from models import Tournament, Player


class TournamentController:

    def __init__(self, tournament):
        self.tournament = tournament

    def start(self):
        TournamentView.display_welcome_message()
        while True:
            choice = TournamentView.display_menu()
            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.add_player()
            elif choice == "3":
                self.start_tournament()
            elif choice == "4":
                self.display_results()
            elif choice == "5":
                print("Au revoir!")
                break
            else:
                print("Choix invalide, veuillez entre le chiffre correspondant à votre requête")

    def create_tournament(self):
        name = input("Nom du tournoi: ")
        location = input("Lieu: ")
        date = input("Date (format JJMMAAAA) : ")
        description = input("Description: ")
        self.tournament = Tournament(name, location, date, description)
        TournamentView.display_tournament_infos(self.tournament)

    def add_player(self):
        family_name = input("Nom: ")
        first_name = input("Prénom: ")
        date_of_birth = input("Date de naissance: ")
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