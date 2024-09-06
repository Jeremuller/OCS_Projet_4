class TournamentView:

    """

      This class provides static methods to display various menus, gather input, and display data related
      to the chess tournament management system.

    """

    @staticmethod
    def display_welcome_message():
        print("Welcome to the chess tournament manager!")

    @staticmethod
    def display_ending_message():
        print("Good bye!")

    @staticmethod
    def display_tournament_conflict_message():
        print("A tournament is already running, please finish or quit it first.")

    @staticmethod
    def display_error_selection_message():
        print("Invalid choice, please enter the number corresponding to your request")

    @staticmethod
    def display_player_saved_out_of_tournament():
        print("There is no tournament running, player saved in file.")

    @staticmethod
    def display_no_player_tournament():
        print("This tournament has no players.")

    @staticmethod
    def display_starting_turn(actual_turn_number, number_of_turn):
        print(f"Starting turn {actual_turn_number} / {number_of_turn} :")

    @staticmethod
    def display_tournament_interrupted():
        print("Tournament interrupted")

    @staticmethod
    def display_back_to_tournament():
        print("Back to tournament.")

    @staticmethod
    def display_invalid_yes_no_choice():
        print("Invalid choice, please enter yes or no.")

    @staticmethod
    def display_tournament_resume(player_list):
        print("\nTournament is over, here is the list of the final scores: ")
        for sorted_player in player_list:
            print(f"Player : {sorted_player.first_name} {sorted_player.family_name}"
                  f" - Points : {sorted_player.points}")

    @staticmethod
    def display_tournament_load_successfully():
        print("Tournament loaded successfully, you can now choose to start it again.")

    @staticmethod
    def display_file_not_found():
        print("File not Found.")

    @staticmethod
    def display_json_decode_error():
        print("Failed to decode JSON file.")

    @staticmethod
    def display_reading_error():
        print(f"Error in reading file.")

    @staticmethod
    def display_id_update_successfully():
        print("Player's national chess number updated successfully.")

    @staticmethod
    def display_menu():

        """

           Displays the main menu and prompts the user to select an option.

           Returns:
               str: The user's choice from the main menu.

        """

        print("\nMain menu:")
        print("1. Create new tournament")
        print("2. Add player")
        print("3. Start tournament")
        print("4. Load tournament")
        print("5. Display datas")
        print("6. Update player national chess number")
        print("7. Quitter")
        main_menu_choice = input("Please enter the number of your choice: ")
        return main_menu_choice

    @staticmethod
    def display_datas_menu():

        """

           Displays the data menu and prompts the user to select an option for displaying various data.

           Returns:
               str: The user's choice from the data menu.

        """

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

        """

            Displays information about a specific tournament.

            Args:
                tournament (Tournament): The tournament object whose information will be displayed.

        """

        print(f"{tournament.name} the {tournament.date} in {tournament.location} : {tournament.description}")

    @staticmethod
    def display_tournaments(tournament_list):

        """

            Displays a list of tournaments with their basic information.

            Args:
                tournament_list (list): A list of Tournament objects.

            Returns:
                int: The index of the tournament displayed.

        """
        index = 0

        # Vérifie d'abord si la liste n'est pas vide
        if not tournament_list:
            print("No tournaments to display.")
            return index

        for index, tournament in enumerate(tournament_list, start=0):
            print(f"{index}. {tournament.name} {tournament.date} "
                  f"{tournament.actual_turn_number}/{tournament.number_of_turns}")
        return index

    @staticmethod
    def display_players(players_list):

        """

           Displays a list of players with their basic information.

           Args:
               players_list (list): A list of Player objects.

        """

        print("\nPlayers list:")
        for index, player in enumerate(players_list, start=0):
            print(f"{index}. {player.family_name} {player.first_name} "
                  f"born {player.date_of_birth} ID {player.national_chess_number}")

    @staticmethod
    def display_turns(turns_list):

        """

           Displays a list of turns with their associated matches.

           Args:
               turns_list (list): A list of Turn objects.

        """

        print("\nTurns list: ")
        for turn in turns_list:
            print(f"{turn.name}")
            for match in turn.matches:
                print(f"{match.match_id} : {match.player1.family_name} {match.player1.first_name} "
                      f"vs {match.player2.family_name} {match.player2.first_name} : result {match.result}")

    @staticmethod
    def get_turn_management_choice():
        user_choice = input("Do you like to get to the next turn ? (yes/no): ").lower()
        return user_choice

    @staticmethod
    def get_quitting_confirmation():
        confirm_exit = input("Are you sure you want to quit the tournament? (yes/no) ").lower()
        return confirm_exit

    @staticmethod
    def get_player_datas():

        """

            Prompts the user to enter the player's details.

            Returns:
                tuple: A tuple containing the family name, first name, date of birth,
                and national chess number of the player.

        """

        print("Please enter the datas of the player you want to register")
        family_name = input("Family name: ")
        first_name = input("First name: ")
        date_of_birth = input("Date of birth (example 04072024): ")
        national_chess_number = input("National chess number: ")
        return family_name, first_name, date_of_birth, national_chess_number

    @staticmethod
    def get_player_index():

        """

            Prompts the user to enter the index of the player whose national chess number they want to update.

            Returns:
                int or None: The index of the player if valid, otherwise None.

        """

        try:
            index = int(input("Please enter the number of the player you want to update national chess number: "))
            return index
        except ValueError:
            print("Invalid input, Please enter a valid number")
            return None

    @staticmethod
    def get_player_national_chess_number():

        """

            Prompts the user to enter the national chess number of a player.

            Returns:
                str: The national chess number entered by the user.

        """

        national_chess_number = input("National chess number:")
        return national_chess_number

    @staticmethod
    def get_tournament_datas():

        """

            Prompts the user to enter the tournament's details.

            Returns:
                tuple: A tuple containing the name, location, date, and description of the tournament.

        """

        print("Please enter the datas of the tournament you want to create")
        name = input("Name: ")
        location = input("Location: ")
        date = input("Date (Example 05092024) : ")
        description = input("Description: ")
        return name, location, date, description

    @staticmethod
    def get_tournament_index():

        """

           Prompts the user to enter the index of the tournament they want to select.

           Returns:
               int or None: The index of the tournament if valid, otherwise None.

        """

        try:
            index = int(input("Please enter the number of the tournament you want to select: "))
            return index
        except ValueError:
            print("Invalid input, Please enter a valid number")
            return None

    @staticmethod
    def get_match_results(match):

        """

            Prompts the user to enter the result of a match.

            Args:
                match (Match): The match for which the result is being entered.

            Returns:
                tuple: A tuple containing the scores for player1 and player2
                based on the result entered by the user.

        """

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
