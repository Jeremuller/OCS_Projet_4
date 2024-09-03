class TournamentView:

    """

      This class provides static methods to display various menus, gather input, and display data related
      to the chess tournament management system.

    """

    @staticmethod
    def display_welcome_message():
        print("Welcome to the chess tournament manager!")

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
        print("6. Update plater national chess number")
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
    def display_tournament(tournament_list):

        """

            Displays a list of tournaments with their basic information.

            Args:
                tournament_list (list): A list of Tournament objects.

            Returns:
                int: The index of the tournament displayed.

        """

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
                print(f"{match.match_id} : {match.player1} vs {match.player2} : result : {match.result}")

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
        date = input("Date () : ")
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
