from views import TournamentView
from models import Tournament, Player, Turn
import json
import os


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
                self.run_tournament()
            elif main_menu_choice == "4":
                self.load_tournament()
            elif main_menu_choice == "5":
                self.informations_menu()
            elif main_menu_choice == "6":
                self.update_national_chess_id()
            elif main_menu_choice == "7":
                self.tournament.save_to_json("archived_tournaments.json")
                print("Good bye!")
                break
            else:
                print("Invalid choice, please enter the number corresponding to your request")

    def tournament_in_progress(self):
        return self.tournament is not None

    def create_tournament(self):
        if self.tournament_in_progress():
            print("A tournament is already running, please finish or quit it first.")

        name, location, date, description = TournamentView.get_tournament_informations()
        self.tournament = Tournament(name, location, date, description)
        TournamentView.display_tournament_info(self.tournament)

    def add_player(self):

        family_name, first_name, date_of_birth, national_chess_number = TournamentView.get_player_informations()
        player = Player(family_name, first_name, date_of_birth, points=0)
        player.national_chess_number = national_chess_number
        player.save_players_to_json("archived_players.json")

        if self.tournament_in_progress():
            self.tournament.add_player(player)
            TournamentView.display_players(self.tournament.players_list)
        else:
            print("There is no tournament running, player saved in file")

    def run_tournament(self):
        # On vérifie d'abord qu'un tournoi a été crée et qu'il comporte des joueurs
        if self.tournament_in_progress():
            if not self.tournament.players_list:
                print("Le tournoi n'a aucun joueur!")
                return

            # Contrôle que le tournoi n'est pas encore terminé
            while self.tournament.actual_turn_number < self.tournament.number_of_turns:
                print(f"Début du tour {self.tournament.actual_turn_number + 1}/{self.tournament.number_of_turns}")

                # Générer les matchs
                turn = self.tournament.create_turn(f"round_{self.tournament.actual_turn_number + 1}")
                matches = turn.generate_matches()

                # Saisie des résultats des matchs
                self.process_match_results(matches)

                # Demander à l'utilisateur s'il souhaite continuer
                while True:
                    continue_choice = input("Do you like to get to the next turn ? (yes/no): ").lower()
                    if continue_choice == "no":
                        confirm_exit = input("Are you sure you want to quit the tournament? (yes/no) ").lower()

                        if confirm_exit == "yes":

                            print("Tournoi interrompu")
                            return
                        else:
                            print("Retour au tournoi.")
                            break
                    elif continue_choice == "yes":
                        self.tournament.actual_turn_number += 1
                        break
                    else:
                        print("Invalid choice, please enter yes or no.")

            # Message de fin de tournoi avec affichage des participants et leurs scores
            print("\nTournament is over, here is the list of the final scores: ")
            self.tournament.save_to_json("archived_tournaments.json")
            sorted_players = sorted(self.tournament.players_list, key=lambda player: player.points, reverse=True)
            for player in sorted_players:
                print(f"Player : {player.first_name} {player.family_name} - Points : {player.points}")

    def load_tournament(self):
        try:
            with open("archived_tournaments.json", "r", encoding="utf-8") as file:
                tournament_list = json.load(file)

                tournament_not_finished = []
                for tournament_data in tournament_list:
                    tournament = Tournament.deserialize_from_dict(tournament_data)

                    if tournament.actual_turn_number < tournament.number_of_turns:
                        tournament_not_finished.append(tournament)

            TournamentView.display_tournament(tournament_not_finished)

            index = TournamentView.get_tournament_index()

            self.tournament = tournament_not_finished[index]
            print("Tournament loaded successfully, you can now choose to start it again.")

        except FileNotFoundError:
            print("File not Found.")

        except json.JSONDecodeError:
            print("Failed to decode JSON file.")

        except IOError as e:
            print(f"Error in reading file {e}")


    def informations_menu(self):
        while True:
            try:
                information_menu_choice = TournamentView.display_informations_menu()
                print(f"DEBUG: Choix utilisateur: {information_menu_choice}")

                if information_menu_choice == "1":
                    print("DEBUG: Afficher les joueurs archivés")  # Debug
                    InformationController.display_archived_players()

                elif information_menu_choice == "2":
                    print("DEBUG: Afficher les tournois archivés")  # Debug
                    InformationController.display_archived_tournaments()

                elif information_menu_choice == "3":
                    print("DEBUG: Afficher les joueurs d'un tournoi")  # Debug
                    InformationController.display_tournament_players()

                elif information_menu_choice == "4":
                    print("DEBUG: Afficher les tours et matchs d'un tournoi")  # Debug
                    InformationController.display_tournament_turns()

                elif information_menu_choice == "5":
                    print("DEBUG: Quitter le menu des informations")  # Debug
                    break

                else:
                    print("Invalid choice, please select a number proposed above.")

            except Exception as e:
                print(f"Erreur inattendue : {e}")
                break

    @staticmethod
    def process_match_results(matches):
        for match in matches:
            score_player1, score_player2 = TournamentView.get_match_results(match)
            match.update_players_points(score_player1, score_player2)

    @staticmethod
    def update_national_chess_id():
        try:
            with open("archived_players.json", "r", encoding="utf-8") as file:
                players_data = json.load(file)
                players_list = [Player.deserialize_from_dict(player_dict) for player_dict in players_data]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error loading players data.")
            return

        TournamentView.display_players(players_list)

        index = TournamentView.get_player_index()

        if index is not None and 0 <= index < len(players_data):
            national_chess_number = TournamentView.get_player_national_chess_number()
            players_data[index]["national_chess_number"] = national_chess_number

            try:
                with open("archived_players.json", "w", encoding="utf-8") as file:
                    json.dump(players_data, file, indent=4)
                print("Player's national chess number updated successfully.")
            except IOError as e:
                print(f"Failed to save data: {e}")
        else:
            print("Invalid player index selected.")


class InformationController:

    @staticmethod
    def display_archived_players():
        file_path = "archived_players.json"

        if not os.path.exists("archived_players.json"):
            print("No file archived players found.")
            return

        with open(file_path, "r", encoding="utf-8") as file:
            try:
                players_data = json.load(file)
                archived_players = [Player.deserialize_from_dict(p) for p in players_data]
                sorted_players_list = sorted(archived_players, key=lambda player: player.family_name)
                TournamentView.display_players(sorted_players_list)
            except json.JSONDecodeError:
                print("Failed to read JSON file.")

    @staticmethod
    def display_archived_tournaments():
        file_path = "archived_tournaments.json"

        if not os.path.exists("archived_tournaments.json"):
            print("No file archived tournaments found")
            return

        with open(file_path, "r", encoding="utf-8") as file:
            try:
                tournaments_data = json.load(file)
                archived_tournaments = [Tournament.deserialize_from_dict(t) for t in tournaments_data]
                print("\n -- Archived tournament list: --")
                for i, tournament in enumerate(archived_tournaments, start=0):
                    print(f"{i}. {tournament.name} - Date: {tournament.date}")

            except json.JSONDecodeError:
                print("Failed to read JSON file.")

    @staticmethod
    def display_tournament_players():
        InformationController.display_archived_tournaments()
        try:
            with open("archived_tournaments.json", "r", encoding="utf-8") as file:
                tournament_data = json.load(file)

            index = TournamentView.get_tournament_index()

            if index is not None and 0 <= index < len(tournament_data):

                players_list = tournament_data[index].get("players_list", [])
                players_data = [Player.deserialize_from_dict(player) for player in players_list]
                sorted_players_list = sorted(players_data, key=lambda player: player.family_name)
                TournamentView.display_players(sorted_players_list)
        except FileNotFoundError:
            print("File not Found.")

        except json.JSONDecodeError:
            print("Failed to decode JSON file.")

        except IOError as e:
            print(f"Error in reading file {e}")

    @staticmethod
    def display_tournament_turns():
        InformationController.display_archived_tournaments()
        try:
            with open("archived_tournaments.json", "r", encoding="utf-8") as file:
                tournament_data = json.load(file)
                print(tournament_data)

            index = TournamentView.get_tournament_index()
            print(index)

            if index is not None and 0 <= index < len(tournament_data):
                turns_data = tournament_data[index].get("turns_list", [])
                turns_list = [Turn.deserialize_from_dict(turn) for turn in turns_data]
                print(turns_list)

                TournamentView.display_turns(turns_list)

        except FileNotFoundError:
            print("File not Found.")

        except json.JSONDecodeError:
            print("Failed to decode JSON file.")

        except IOError as e:
            print(f"Error in reading file {e}")






"""def integration_test():

    players_list = [
        Player(first_name="Magnus", family_name="Carlsen", date_of_birth="30111990"),
        Player(first_name="Hikaru", family_name="Nakamura", date_of_birth="09121987"),
        Player(first_name="Fabiano", family_name="Caruana", date_of_birth="30111992"),
        Player(first_name="Ian", family_name="Nepomniachtchi", date_of_birth="14071990")
    ]

    players_list[0].national_chess_number = "NOR19901130"
    players_list[1].national_chess_number = "USA19871209"
    players_list[2].national_chess_number = "USA19921130"
    players_list[3].national_chess_number = "RUS19900714"

    print("Initial list of players:")
    print(str(players_list))

    tournament = Tournament(
        name="Grand chess Tournament",
        location="Paris",
        date="25082024",
        description="2024's edition Grand Chess Tournament"
    )

    for player in players_list:
        tournament.add_player(player)

    first_turn = tournament.create_turn("Round_1")
    first_turn.generate_matches()

    print("\nInitial tournament data:")
    print(tournament)

    test_file = "tournament_test.json"
    tournament.save_to_json(test_file)

    loaded_data = Tournament.load_from_json(test_file)

    if isinstance(loaded_data, list):
        print("loaded_data est une liste.")
    else:
        print("loaded_data n'est pas une liste.")

    deserialized_tournaments = [Tournament.deserialize_from_dict(tournament_data) for tournament_data in loaded_data]

    print("\nDeserialized tournament data:")
    for deserialized_tournament in deserialized_tournaments:
        print(f"{deserialized_tournament.name} {deserialized_tournament.date} "
              f"{deserialized_tournament.location} {deserialized_tournament.players_list}")

    os.remove("tournament_test.json")

    print("test réussi")


integration_test()"""


# Point d'entrée du programme
if __name__ == "__main__":
    controller = TournamentController()
    controller.start()
