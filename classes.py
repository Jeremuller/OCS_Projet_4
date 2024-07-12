"""Instanciation de la classe joueur"""

class Player:
    def __init__(self, family_name, first_name, date_of_birth, national_chess_number, points):
        self.family_name = family_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.national_chess_number = national_chess_number
        self.points = points

"""Instanciation de la classe tournoi"""

class Tournament:
    def __init__(self, name, location, actual_turn_number, turns_list, players_list, description, number_of_turns=4):
        self.name = name
        self.location = location
        self.actual_turn_number = actual_turn_number
        self.turns_list = turns_list
        self.players_list = players_list
        self.description = description
        self.number_of_turns = number_of_turns

    def match_making(self):
        while actual_turn_number < number_of_turns:

# trier la players list, et faire des paires par ordre croissant de points, penser au cas où ils se sont déjà rencontrés


"""Instanciation de la classe match """

class Match:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def match_results(self, player1, player2):
            if player1 win = True
                player1.points +=1
                player2.points -=1
            elif:
                player2.points +=1
                player1.points -=1
            else:
                player1.points +=0.5
                player2.points +=0.5