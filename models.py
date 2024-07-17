
class Player:

    """ Déclaration de la classe joueur """

    def __init__(self, family_name, first_name, date_of_birth, points):
        self.family_name = family_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.national_chess_number = None
        self.points = points

    def add_national_chess_number(self, national_chess_number):
        self.national_chess_number = national_chess_number


class Tournament:

    """ Déclaration de la classe tournoi """

    def __init__(self, name, location, description, actual_turn_number=0, turns_list=None, players_list=None,
                 number_of_turns=4):
        self.name = name
        self.location = location
        self.description = description
        self.actual_turn_number = actual_turn_number
        self.turns_list = turns_list
        self.players_list = players_list
        self.number_of_turns = number_of_turns

    def add_player(self, player):
        self.players_list.append(player)

    def add_turn(self, turn):
        self.turns_list.append(turn)


class Match:

    """ Déclaration de la classe match """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None


class Turn:

    """ Déclaration de la classe tour """

    def __init__(self, name):
        self.name = name
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def get_results(self):
        results = []
        for match in self.matches:
            results.append(match.match_result())
        return results


class TournamentList:
    tournament_list = []
    pass

    def update_tournament_list(self, tournament):
        TournamentList.append(tournament)


