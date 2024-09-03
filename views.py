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
        print("4. Load tournament")
        print("5. Display datas")
        print("6. Update plater national chess number")
        print("7. Quitter")
        main_menu_choice = input("Please enter the number of your choice: ")
        return main_menu_choice

    @staticmethod
    def display_datas_menu():
        print("\nDisplay datas:")
        print("1. Display archived players")
        print("2. Display archived tournaments")
        print("3. Display tournament's players")
        print("4. Display tournament's turns")
        print("5. Back to main menu")

        information_menu_choice = input("Please enter the number of your choice: ")
        print(information_menu_choice)
        return str(information_menu_choice)

    @staticmethod
    def display_tournament_info(tournament):
        print(f"{tournament.name} the {tournament.date} in {tournament.location} : {tournament.description}")

    @staticmethod
    def display_tournament(tournament_list):
        for index, tournament in enumerate(tournament_list, start=0):
            print(f"{index}. {tournament.name} {tournament.date} "
                  f"{tournament.actual_turn_number}/{tournament.number_of_turns}")
            return index

    @staticmethod
    def display_players(players_list):
        print("\nPlayers list:")
        for index, player in enumerate(players_list, start=0):
            print(f"{index}. {player.family_name} {player.first_name} "
                  f"born {player.date_of_birth} ID {player.national_chess_number}")

    @staticmethod
    def display_turns(turns_list):
        print("\nTurns list: ")
        for turn in turns_list:
            print(f"{turn.name}")
            for match in turn.matches:
                print(f"{match.match_id} : {match.player1} vs {match.player2} : result : {match.result}")

    @staticmethod
    def get_player_datas():
        print("Please enter the datas of the player you want to register")
        family_name = input("Family name: ")
        first_name = input("First name: ")
        date_of_birth = input("Date of birth (example 04072024): ")
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
    def get_tournament_datas():
        print("Please enter the datas of the tournament you want to create")
        name = input("Name: ")
        location = input("Location: ")
        date = input("Date () : ")
        description = input("Description: ")
        return name, location, date, description

    @staticmethod
    def get_tournament_index():
        try:
            index = int(input("Please enter the number of the tournament you want to select: "))
            return index
        except ValueError:
            print("Invalid input, Please enter a valid number")
            return None

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
