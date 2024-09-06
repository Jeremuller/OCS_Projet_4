import random
import json
import os


class Player:

    """Declaration of the Player class.

    Attributes:
        family_name (str): The family name of the player.
        first_name (str): The first name of the player.
        date_of_birth (str): The date of birth of the player.
        points (int): The points scored by the player. Defaults to 0.
        national_chess_number (str or None): the national chess number of the player. Defaults to
        None but can be added afterward by the Main menu.
    """

    def __init__(self, family_name, first_name, date_of_birth, points=0):

        """
        Initializes a new Player instance.

        Args:
            family_name (str): The family name of the player.
            first_name (str): The first name of the player.
            date_of_birth (str): The date of birth of the player.
            points (int, optional): The initial points of the player. Defaults to 0.
        """

        self.family_name = family_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.points = points
        self.national_chess_number = None

    def serialize_to_dict(self):

        """
                Serializes the player instance to a dictionary.

                Returns:
                    dict: A dictionary representation of the player.
        """

        return {
            "first_name": self.first_name,
            "family_name": self.family_name,
            "date_of_birth": self.date_of_birth,
            "points": self.points,
            "national_chess_number": self.national_chess_number
        }

    def save_player_to_json(self, file_path):

        """
               Saves the player's data to a JSON file. Check if teh player already exists to update datas.

               Args:
                   file_path (str): The path to the JSON file where the player's data will be saved.
       """

        try:
            if os.path.exists(file_path):
                # Load existing players data if the file exists
                with open(file_path, "r", encoding="utf-8") as file:
                    try:
                        players_data = json.load(file)
                        if not isinstance(players_data, list):
                            players_data = [players_data]
                    except json.JSONDecodeError:
                        players_data = []
            else:
                players_data = []

            player_data = self.serialize_to_dict()

            player_found = False

            for index, player in enumerate(players_data):
                # Check if the player isn't already saved in the file
                if (player["first_name"] == player_data["first_name"]
                   and player["family_name"] == player_data["family_name"]):
                    players_data[index] = player_data
                    player_found = True
                    break

            if not player_found:
                players_data.append(player_data)
            # Save a new version of the file with the new player in it
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(players_data, file, indent=4)
            print(f"All data have been saved in {file_path} successfully.")

        except IOError as e:
            print(f"Failed to save data: {e}.")

    @classmethod
    def deserialize_from_dict(cls, data):

        """
                Creates a Player instance from a dictionary.

                Args:
                    data (dict): A dictionary containing player data.

                Returns:
                    Player: A Player instance created from the provided data.
        """

        player = cls(
            family_name=data["family_name"],
            first_name=data["first_name"],
            date_of_birth=data["date_of_birth"],
        )
        player.points = data.get("points")
        player.national_chess_number = data.get("national_chess_number")
        return player

    def add_national_chess_number(self, national_chess_number):

        """
               Adds a national chess number to the player.

               Args:
                   national_chess_number (str): The national chess number to assign to the player.
       """

        self.national_chess_number = national_chess_number


class Tournament:

    """

    Declaration of the Tournament class

    Attributes:
        name (str): The name of the tournament.
        location (str): The location where the tournament is held.
        date (str): The date of the tournament.
        description (str): A brief description of the tournament.
        actual_turn_number (int): The current turn number in the tournament.
        number_of_turns (int): The total number of turns in the tournament.
        players_list (list): A list of players participating in the tournament.
        turns_list (list): A list of turns in the tournament.

    """

    def __init__(self, name, location, date, description, actual_turn_number=0,  number_of_turns=4):

        """

       Initializes a new Tournament instance.

       Args:
           name (str): The name of the tournament.
           location (str): The location of the tournament.
           date (str): The date of the tournament.
           description (str): The description of the tournament.
           actual_turn_number (int, optional): The current turn number. Defaults to 0.
           number_of_turns (int, optional): The total number of turns. Defaults to 4.

       """

        self.name = name
        self.location = location
        self.date = date
        self.description = description
        self.actual_turn_number = actual_turn_number
        self.number_of_turns = number_of_turns
        self.players_list = []
        self.turns_list = []

    def add_player(self, player):

        """

            Adds a player to the tournament's players list.

            Args:
                player (Player): The player to add to the tournament.

        """

        self.players_list.append(player)

    def create_turn(self, name):

        """

            Creates a new turn and adds it to the tournament's turns list.

            Args:
                name (str): The name of the turn.

            Returns:
                Turn: The newly created turn.

        """

        turn = Turn(name, self.players_list)
        self.turns_list.append(turn)
        return turn

    def serialize_to_dict(self):

        """

            Serializes the tournament instance to a dictionary.

            Returns:
                dict: A dictionary representation of the tournament.

        """

        return {
            "name": self.name,
            "location": self.location,
            "date": self.date,
            "description": self.description,
            "actual_turn_number": self.actual_turn_number,
            "number_of_turns": self.number_of_turns,
            "players_list": [player.serialize_to_dict() for player in self.players_list],
            "turns_list": [turn.serialize_to_dict()for turn in self.turns_list]
        }

    def save_to_json(self, file_path):

        """

            Saves the tournament's data to a JSON file. If a tournament with the same
            name, location, and date already exists, it will be updated with the new data.

            Args:
            file_path (str): The path to the JSON file where the tournament's data will be saved.

        """

        if os.path.exists(file_path):
            # Load existing tournaments data if the file exists
            with open(file_path, "r", encoding="utf-8") as file:
                try:
                    tournaments_data = json.load(file)
                except json.JSONDecodeError:
                    tournaments_data = []

        else:
            tournaments_data = []

        tournament_data = self.serialize_to_dict()

        tournament_found = False

        # Check if a tournament with the same name, location and date already exists
        for index, tournament in enumerate(tournaments_data):
            if (tournament["name"] == tournament_data["name"]
                    and tournament["location"] == tournament_data["location"]
                    and tournament["date"] == tournament_data["date"]):
                # Update the existing tournament_data
                tournaments_data[index] = tournament_data
                tournament_found = True
                break

        if not tournament_found:
            tournaments_data.append(tournament_data)

        try:
            # Save the new tournament data file with the new tournament added
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(tournaments_data, file, indent=4)
                print(f"Tournament successfully saved in {file_path}.")
        except IOError as e:
            print(f"Failed to save JSON file: {e}")

    @classmethod
    def deserialize_from_dict(cls, data):

        """

            Creates a Tournament instance from a dictionary.

            Args:
                data (dict): A dictionary containing tournament data.

            Returns:
                Tournament: A Tournament instance created from the provided data.

        """

        tournament = cls(
            name=data["name"],
            location=data["location"],
            date=data["date"],
            description=data["description"],
            actual_turn_number=data["actual_turn_number"],
            number_of_turns=data["number_of_turns"],
        )
        tournament.players_list = [Player.deserialize_from_dict(player_data)
                                   for player_data in data.get("players_list", [])]
        tournament.turns_list = [Turn.deserialize_from_dict(turn_data) for turn_data in data.get("turns_list", [])]
        return tournament

    @classmethod
    def load_from_json(cls, file_path):

        """

           Loads tournament data from a JSON file.

           Args:
               file_path (str): The path to the JSON file to load.

           Returns:
               list: A list of tournament data if the file is successfully loaded.

       """

        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                print(f"File load successfully from {file_path}.")
                return data
        except IOError as e:
            print(f"Failed to read JSON file named: {e}")
        except json.JSONDecodeError as e:
            print(f"Failed do decode JSON file named: {e}")


class Match:

    """

    Declaration of the Match class

    Attributes:
        match_id (str): The unique identifier for the match.
        player1 (Player): The first player in the match.
        player2 (Player): The second player in the match.
        result (tuple or None): The result of the match as a tuple of scores. Defaults to None.

    """

    def __init__(self, match_id, player1, player2):

        """

            Initializes a new Match instance.

            Args:
                match_id (str): The unique identifier for the match.
                player1 (Player): The first player in the match.
                player2 (Player): The second player in the match.

        """

        self.player1 = player1
        self.player2 = player2
        self.match_id = match_id
        self.result = None

    def update_players_points(self, player1_score, player2_score):

        """

           Updates the points of both players based on the match result.

           Args:
               player1_score (int): The score of the first player.
               player2_score (int): The score of the second player.

       """

        self.result = (player1_score, player2_score)
        self.player1.points += player1_score
        self.player2.points += player2_score

    def serialize_to_dict(self):

        """

           Serializes the match instance to a dictionary.

           Returns:
               dict: A dictionary representation of the match.

        """

        return {
            "match_id": self.match_id,
            "player1": self.player1.serialize_to_dict(),
            "player2": self.player2.serialize_to_dict(),
            "result": self.result
        }

    def save_to_json(self, file_path):

        """

           Saves the match's data to a JSON file.

           Args:
              file_path (str): The path to the JSON file where the match's data will be saved.

        """

        try:
            match_data = self.serialize_to_dict()

            with open(file_path, "w") as file:
                json.dump(match_data, file, indent=4)
        except IOError as e:
            print(f"Failed to save JSON file named: {e}")

    @classmethod
    def deserialize_from_dict(cls, data):

        """

           Creates a Match instance from a dictionary.

           Args:
               data (dict): A dictionary containing match data.

           Returns:
               Match: A Match instance created from the provided data.

        """

        player1 = Player.deserialize_from_dict(data["player1"])
        player2 = Player.deserialize_from_dict(data["player2"])
        match = cls(data["match_id"], player1, player2)
        match.result = data["result"]
        return match


class Turn:
    """

        Declaration of the Turn class.

        Attributes:
            name (str): The name of the turn.
            players_list (list): A list of players participating in the turn.
            matches (list): A list of matches in the turn.
            previous_matches (list): A list of matches from previous turns. Defaults to an empty list.

    """

    def __init__(self, name, players_list, previous_matches=None):

        """

           Initializes a new Turn instance.

           Args:
               name (str): The name of the turn.
               players_list (list): The list of players for this turn.
               previous_matches (list, optional): The list of previous matches. Defaults to None.

        """

        self.name = name
        self.players_list = players_list
        self.matches = []
        self.previous_matches = previous_matches if previous_matches else []

    # A function that will handle the matchmaking
    def generate_matches(self):

        """

           Generates matches for the turn based on player standings and previous matches.

           Returns:
               list: A list of Match objects representing the matches for the turn.

        """

        playing_players = self.players_list.copy()

        if self.name == "round_1":
            # Shuffle players randomly for the first round
            random.shuffle(playing_players)
        else:
            #  Sort players by their points in descending order
            playing_players.sort(key=lambda player: player.points, reverse=True)
            i = 0
            while i < len(playing_players) - 1:
                j = i
                while j < len(playing_players) - 1 and playing_players[j].points == playing_players[j + 1].points:
                    j += 1
                if j > i and (j - i + 1) > 2:
                    # Shuffle players with the same score to randomize pairings
                    random.shuffle(playing_players[i:j + 1])
                i = j + 1

        matches = []
        i = 0
        while i < len(playing_players) - 1:
            player1 = playing_players[i]
            player2 = None

            # Look for a player which haven't played against player1 yet
            for j in range(i + 1, len(playing_players)):
                potential_opponent = playing_players[j]
                if not self.has_played_before(player1, potential_opponent):
                    player2 = potential_opponent
                    break

            # If we've found an opponent
            if player2:
                match_id = f"{self.name}_match_{i + 1}"
                matches.append(Match(match_id, player1, player2))
                playing_players.remove(player2)
            else:
                # Pair player1 one with the next player if no unique opponent is found
                match_id = f"{self.name}_match_{i + 1}"
                matches.append(Match(match_id, player1, playing_players[i + 1]))
            i += 1

        self.matches = matches
        return matches

    def has_played_before(self, player1, player2):

        """

            Checks if two players have played against each other before in previous matches.

            Args:
                player1 (Player): The first player.
                player2 (Player): The second player.

            Returns:
                bool: True if the players have played before, False otherwise.

        """

        for match in self.previous_matches:
            if (match.player1 == player1 and match.player2 == player2) or \
               (match.player1 == player2 and match.player2 == player1):
                return True
        return False

    def serialize_to_dict(self):

        """

            Serializes the turn instance to a dictionary.

        Returns:
            dict: A dictionary representation of the turn.

        """

        return {
            "name": self.name,
            "players_list": [player.serialize_to_dict() for player in self.players_list],
            "matches": [match.serialize_to_dict() for match in self.matches]
        }

    def save_to_json(self, file_path):

        """

            Saves the turn's data to a JSON file.

            Args:
                file_path (str): The path to the JSON file where the turn's data will be saved.

        """

        try:
            turn_data = self.serialize_to_dict()

            with open(file_path, "w") as file:
                json.dump(turn_data, file, indent=4)
        except IOError as e:
            print(f"Failed to save JSON file named: {e}")

    @classmethod
    def deserialize_from_dict(cls, data):

        """

            Creates a Turn instance from a dictionary.

            Args:
                data (dict): A dictionary containing turn data.

            Returns:
                Turn: A Turn instance created from the provided data.

        """

        players_list = [Player.deserialize_from_dict(player_data) for player_data in data["players_list"]]
        turn = cls(data["name"], players_list)
        turn.matches = [Match.deserialize_from_dict(match_data) for match_data in data["matches"]]
        return turn
