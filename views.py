from models import Turn


class TournamentView:

    @staticmethod
    def display_welcome_message():
        print("Welcome to the chess tournament manager!")

    @staticmethod
    def display_menu():
        print("\nMain menu:")
        print("1. Create new tournament")
        print("2. Add player")
        print("3. Start tournament")
        print("4. Display informations")
        print("5. Update plater national chess number")
        print("6. Quitter")
        main_menu_choice = input("Please enter the number of your choice: ")
        return main_menu_choice

    @staticmethod
    def display_informations_menu():
        print("\nDisplay informations:")
        print("1. Display tournament's informations")
        print("2. Display tournament's players")
        print("3. Display tournament's rounds and matches")
        print("4. Display on file players")
        print("5. Display on file tournaments")
        print("6. Back to main menu")
        informations_menu_choice = input("Please enter the number of your choice: ")
        return informations_menu_choice

    @staticmethod
    def load_turns_data():
        turns_data = Turn.serialize_to_dict("turns_list.json")
        return turns_data

    @staticmethod
    def display_tournament_infos(tournament):
        print(f"\nTournament's details: {tournament.name}:")
        print(f"Date: {tournament.date}")

    @staticmethod
    def display_players(players_list):
        print("\nPlayers list:")
        for index, player in enumerate(players_list, start=0):
            print(f"{index}. {player.family_name} {player.first_name} "
                  f"born {player.date_of_birth} ID {player.national_chess_number}")

    @staticmethod
    def display_tournament_turns(tournament):
        print(f"\n Tournament's turns {tournament.name}:")
        for turn in tournament.turns_list:
            print(turn.name)
            for turn.match in turn.matches:
                print(str(turn.match))

    @staticmethod
    def display_match_results(matches):
        print("\nMatches results: ")
        for match in matches:
            print(f"{match.player1} vs {match.player2} ->> winner: {match.result}")

    @staticmethod
    def get_player_informations():
        print("Please enter the informations of the player you want to register")
        family_name = input("Family name: ")
        first_name = input("First name: ")
        date_of_birth = input("Date of birth (format JJMMAAAA): ")
        national_chess_number = input("National chess number: ")
        return family_name, first_name, date_of_birth, national_chess_number

    @staticmethod
    def get_player_index():
        try:
            index = int(input("Please enter the number of the player you want to update national chess number: "))
            return index
        except ValueError:
            print("Invalid input, Please enter a valid number")
            return None

    @staticmethod
    def get_player_national_chess_number():
        national_chess_number = input("National chess number:")
        return national_chess_number

    @staticmethod
    def get_tournament_informations():
        print("Please enter the informations of the tournament you want to create")
        name = input("Name: ")
        location = input("Location: ")
        date = input("Date (format MMDDYYYY) : ")
        description = input("Description: ")
        return name, location, date, description

    @staticmethod
    def get_match_results(match):
        while True:
            print(f"Match: {match.player1.family_name} {match.player1.first_name} vs "
                  f"{match.player2.family_name} {match.player2.first_name}")
            result = input(f"Did player: {match.player1.family_name} {match.player1.first_name} "
                           "won? (yes/no/draw in case of draw): ").lower()

            if result == "yes":
                return 1, 0
            elif result == "no":
                return 0, 1
            elif result == "draw":
                return 0.5, 0.5
            else:
                print("Invalid result, may enter yes, no or draw")
