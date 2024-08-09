import random


class Player:

    """Déclaration de la classe joueur"""

    def __init__(self, family_name, first_name, date_of_birth, points=0):
        self.family_name = family_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.points = points
        self.national_chess_number = None

    def add_national_chess_number(self, national_chess_number):
        self.national_chess_number = national_chess_number

    def __repr__(self):
        return f"{self.family_name} {self.first_name}, ID: {self.national_chess_number}, Points: {self.points}"


class FinishedTournamentException(Exception):
    pass


class IncorrectMatchResultException(Exception):
    pass


class Tournament:

    """Déclaration de la classe tournoi"""

    def __init__(self, name, location, date, description, actual_turn_number=0,  number_of_turns=4):

        self.name = name
        self.location = location
        self.date = date
        self.description = description
        self.actual_turn_number = actual_turn_number
        self.number_of_turns = number_of_turns
        self.players_list = []
        self.turns_list = []

    def add_player(self, player):
        self.players_list.append(player)

    def create_turn(self, name):
        if self.actual_turn_number >= self.number_of_turns:
            raise FinishedTournamentException("Le tournoi est terminé, aucun match ne peut être joué")
        turn = Turn(name, self.players_list)
        self.turns_list.append(turn)
        self.actual_turn_number += 1
        return turn

    def __str__(self):
        return (f"Tournament: {self.name}, Location: {self.location}, Date: {self.date}, "
                f"Description: {self.description}, Current Turn: {self.actual_turn_number}/{self.number_of_turns}")


class Match:

    """Déclaration de la classe match"""

    def __init__(self, match_id, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.match_id = match_id
        self.result = None

    def match_result(self, result):
        if result == self.player1:
            self.player1.points += 1
            self.player2.points -= 1
        elif result == self.player2:
            self.player2.points += 1
            self.player1.points -= 1
        elif result == "draw":
            self.player1.points += 0.5
            self.player2.points += 0.5
        else:
            raise IncorrectMatchResultException(
                "Le résultat doit impérativement comporter le nom du joueur1 du joueur2, ou 'draw'")
        self.result = result

    def __str__(self):
        return f"{self.match_id}: {self.player1} vs {self.player2}, Result: {self.result}"


class Turn:

    """Déclaration de la classe tour"""

    def __init__(self, name, players_list, previous_matches=None):
        self.name = name
        self.players_list = players_list
        self.matches = []
        self.previous_matches = previous_matches if previous_matches else []

    # Déclaration d'une fonction qui va définir les matchs pour un nouveau tour
    def generate_matches(self):
        if self.name == "round_1":
            # Mélange les joueurs aléatoirement pour le premier tour
            random.shuffle(self.players_list)
        else:
            #  Tri de la liste de joueurs en fonction de leur nombre de points
            self.players_list.sort(key=lambda player: player.points, reverse=True)
            i = 0
            while i < len(self.players_list) - 1:
                j = i
                while j < len(self.players_list) - 1 and self.players_list[j].points == self.players_list[j + 1].points:
                    j += 1
                if j > i and (j - i + 1) > 2:
                    random.shuffle(self.players_list[i:j + 1])
                i = j + 1

        matches = []
        i = 0
        while i < len(self.players_list) - 1: 
            player1 = self.players_list[i]
            player2 = None

            # Cherche un adversaire qui n'a pas déjà joué contre player1
            for j in range(i + 1, len(self.players_list)):
                potential_opponent = self.players_list[j]
                if not self.has_played_before(player1, potential_opponent):
                    player2 = potential_opponent
                    break

            # Si on a trouvé un adversaire valide
            if player2:
                match_id = f"{self.name}_match_{i + 1}"
                matches.append(Match(match_id, player1, player2))
                self.players_list.remove(player2)
            else:
                # Pas d'adversaire disponible (cas improbable mais à gérer)
                match_id = f"{self.name}_match_{i + 1}"
                matches.append(Match(match_id, player1, self.players_list[i+1]))
            i += 1

        self.matches = matches
        return matches

    def has_played_before(self, player1, player2):
        for match in self.previous_matches:
            if (match.player1 == player1 and match.player2 == player2) or \
               (match.player1 == player2 and match.player2 == player1):
                return True
        return False

    def __str__(self):
        return f"Turn: {self.name}, Matches: {[str(match) for match in self.matches]}"
