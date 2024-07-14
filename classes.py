"""Instanciation de la classe joueur"""

class Player:
    def __init__(self, family_name, first_name, date_of_birth, national_chess_number, points):
        self.family_name = family_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.national_chess_number = national_chess_number
        self.points = points

    def display_info(self):
        return f"{self.family_name} {self.first_name}, date of birth: {self.date_of_birth}, ID: {self.national_chess_number}, points: {self.points}"

    def update_points(self, points):
        self.points += points


"""Instanciation de la classe tournoi"""

class Tournament:
    def __init__(self, name, location, description, actual_turn_number=0, turns_list=None, players_list=None, number_of_turns=4):
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

# Déclaration d'une fonction qui va définir les matchs entre deux tours
    def match_making(self):
        # D'abord on vérifie s'il reste au moins un tour à jouer
        if self.actual_turn_number < self.number_of_turns:
            # Ensuite on va trier notre liste de joueurs en fonction de leur nombre de points
            self.players_list.sort(key=lambda player: player.points)
            # Maintenant on fait des paires par ordre croissant de points
            pairs = []
            for i in range(0, len(self.players_list), 2):
                if i+1 < len(self.players_list):
                    pairs.append(self.players_list[i], self.players_list[i+1])
            # Reste à ajouter un fonction qui teste si nos paires se sont déjà rencontrées
            return pairs
        else:
            print("Le tournoi est terminé, merci à tous d'avoir participé!")


"""Instanciation de la classe match """

class Match:
    def __init__(self, player1, player2, result):
        self.player1 = player1
        self.player2 = player2
        self.result = None

    def match_result(self, result):
        if result == "player1":
            self.player1.points += 1
            self.player2.points -= 1
        elif result == "player2":
            self.player2.points += 1
            self.player1.points -= 1
        elif result == "draw":
            self.player1.points += 0.5
            self.player2.points += 0.5
        else:
            raise ValueError("Le résultat doit impérativement comporter le nom du joueur1 du joueur2, ou 'draw'")
        self.result = result