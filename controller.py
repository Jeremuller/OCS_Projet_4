from views import TournamentView
from models import Tournament, Player, Turn
import json
import os


class TournamentController:

    """

        This class handles the main operations of the chess tournament manager,
        including creating tournaments, adding players, running tournaments,
        loading archived data, and updating player information.

    """

    def __init__(self):
        self.view = TournamentView()
        self.tournament = None

    def start(self):

        """

            Starts the tournament management program, displaying the welcome message
            and main menu, and directing the user based on their menu choices.

        """

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
                self.datas_menu()
            elif main_menu_choice == "6":
                self.update_national_chess_id()
            elif main_menu_choice == "7":
                self.tournament.save_to_json("archived_tournaments.json")
                print("Good bye!")
                break
            else:
                print("Invalid choice, please enter the number corresponding to your request")

    def tournament_in_progress(self):

        """

            Checks if a tournament is currently in progress.

            Returns:
                bool: True if a tournament is in progress, False otherwise.

        """

        return self.tournament is not None

    def create_tournament(self):

        """

           Creates a new tournament if none is currently in progress.
           Prompts the user for tournament details and initializes a new Tournament object.

        """

        if self.tournament_in_progress():
            print("A tournament is already running, please finish or quit it first.")

        name, location, date, description = TournamentView.get_tournament_datas()
        self.tournament = Tournament(name, location, date, description)
        TournamentView.display_tournament_info(self.tournament)

    def add_player(self):

        """

            Adds a new player to the current tournament or archives the player
            if no tournament is in progress.

        """

        family_name, first_name, date_of_birth, national_chess_number = TournamentView.get_player_datas()
        player = Player(family_name, first_name, date_of_birth, points=0)
        player.national_chess_number = national_chess_number
        player.save_players_to_json("archived_players.json")

        if self.tournament_in_progress():
            self.tournament.add_player(player)
            TournamentView.display_players(self.tournament.players_list)
        else:
            print("There is no tournament running, player saved in file.")

    def run_tournament(self):

        """

            Runs the current tournament, handling turn progression, match results,
            and checking if the tournament has been completed.

        """

        # First we check if a tournament isn't already running, and then if it has players in it
        if self.tournament_in_progress():
            if not self.tournament.players_list:
                print("This tournament has no players.")
                return

            # Check tournament's turns to see if we can continue running
            while self.tournament.actual_turn_number < self.tournament.number_of_turns:
                print(f"Starting turn {self.tournament.actual_turn_number + 1}/{self.tournament.number_of_turns}")

                # Generate matches for the current turn
                turn = self.tournament.create_turn(f"round_{self.tournament.actual_turn_number + 1}")
                matches = turn.generate_matches()

                # Set match results
                self.process_match_results(matches)
                self.tournament.actual_turn_number += 1
                # Ask if the user wants to continue to the next turn
                while True:
                    continue_choice = input("Do you like to get to the next turn ? (yes/no): ").lower()
                    if continue_choice == "no":
                        confirm_exit = input("Are you sure you want to quit the tournament? (yes/no) ").lower()

                        if confirm_exit == "yes":

                            print("Tournament interrupted")
                            return
                        else:
                            print("Back to tournament.")
                            break
                    elif continue_choice == "yes":

                        break
                    else:
                        print("Invalid choice, please enter yes or no.")

            # Tournament ending message with a resume of the player's scores
            print("\nTournament is over, here is the list of the final scores: ")
            self.tournament.save_to_json("archived_tournaments.json")
            sorted_players = sorted(self.tournament.players_list, key=lambda player: player.points, reverse=True)
            for sorted_player in sorted_players:
                print(f"Player : {sorted_player.first_name} {sorted_player.family_name}"
                      f" - Points : {sorted_player.points}")

    def load_tournament(self):

        """

            Loads a tournament from the archive if it has not been completed.

        """

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

    @staticmethod
    def datas_menu():

        """

            Displays the data menu to the user and handles data display choices.

        """

        while True:
            information_menu_choice = TournamentView.display_datas_menu()

            if information_menu_choice == "1":
                InformationController.display_archived_players()

            elif information_menu_choice == "2":
                InformationController.display_archived_tournaments()

            elif information_menu_choice == "3":
                InformationController.display_tournament_players()

            elif information_menu_choice == "4":
                InformationController.display_tournament_turns()

            elif information_menu_choice == "5":
                break

            else:
                print("Invalid choice, please select a number proposed above.")

    @staticmethod
    def process_match_results(matches):

        """

            Processes the results of matches, updating player points accordingly.

            Args:
                matches (list): A list of Match objects to process.

        """

        for match in matches:
            score_player1, score_player2 = TournamentView.get_match_results(match)
            match.update_players_points(score_player1, score_player2)

    @staticmethod
    def update_national_chess_id():

        """

           Allows the user to update a player's national chess number.

        """

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

    """

        This class handles the display of archived players and tournaments, as well as
        the display of players and turns for a specific tournament.

    """

    @staticmethod
    def display_archived_players():

        """

            Displays a list of all archived players sorted by family name.

        """

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

        """

            Displays a list of all archived tournaments.

        """

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

        """

            Displays the players of a selected archived tournament.

        """

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

        """

           Displays the turns of a selected archived tournament.

        """

        InformationController.display_archived_tournaments()
        try:
            with open("archived_tournaments.json", "r", encoding="utf-8") as file:
                tournament_data = json.load(file)

            index = TournamentView.get_tournament_index()

            if index is not None and 0 <= index < len(tournament_data):
                turns_data = tournament_data[index].get("turns_list", [])
                turns_list = [Turn.deserialize_from_dict(turn) for turn in turns_data]

                TournamentView.display_turns(turns_list)

        except FileNotFoundError:
            print("File not Found.")

        except json.JSONDecodeError:
            print("Failed to decode JSON file.")

        except IOError as e:
            print(f"Error in reading file {e}")


# Program entry point
if __name__ == "__main__":
    controller = TournamentController()
    controller.start()
