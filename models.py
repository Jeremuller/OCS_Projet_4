
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

    def update_points(self, score):
        self.points += score

    def __str__(self):
        return f"{self.family_name} {self.first_name}, ID: {self.national_chess_number}, Points: {self.points}"


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

    def add_turn(self, turn):
        self.turns_list.append(turn)
        self.actual_turn_number += 1

    # Déclaration d'une fonction qui va définir les matchs pour un nouveau tour
    def match_making(self):
        # D'abord on vérifie s'il reste au moins un tour à jouer
        if self.actual_turn_number < self.number_of_turns:
            # Ensuite on va trier notre liste de joueurs en fonction de leur nombre de points
            self.players_list.sort(key=lambda player: player.points)
            # Maintenant on fait des paires par ordre croissant de points
            pairs = []
            for i in range(0, len(self.players_list), 2):
                if i + 1 < len(self.players_list):
                    pairs.append(self.players_list[i], self.players_list[i + 1])
            # Reste à ajouter une fonction qui teste si nos paires se sont déjà rencontrées
            return pairs
        else:
            print("Le tournoi est terminé, merci à tous d'avoir participé!")

    def __str__(self):
        return (f"Tournament: {self.name}, Location: {self.location}, Date: {self.date}, "
                f"Description: {self.description}, Current Turn: {self.actual_turn_number}/{self.number_of_turns}")


class Match:

    """Déclaration de la classe match"""

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.result = None
        self.outcome = None

    def match_result(self, outcome):
        if outcome == self.player1:
            self.player1.points += 1
            self.player2.points -= 1
        elif outcome == self.player2:
            self.player2.points += 1
            self.player1.points -= 1
        elif outcome == "draw":
            self.player1.points += 0.5
            self.player2.points += 0.5
        else:
            raise ValueError("Le résultat doit impérativement comporter le nom du joueur1 du joueur2, ou 'draw'")
        self.outcome = outcome

    def __str__(self):
        return f"Match: {self.player1} vs {self.player2}, Result: {self.result}"


class Turn:

    """Déclaration de la classe tour"""

    def __init__(self, name):
        self.name = name
        self.matches = []

    def add_match(self, match):
        self.matches.append(match)

    def get_results(self):
        results = []
        for Match.match in self.matches:
            results.append(match.match_result())
        return results

    def __str__(self):
        return f"Turn: {self.name}, Matches: {[str(match) for Match.match in self.matches]}"


blunt_roger_1982 = Player("blunt", "roger", 1982)
doe_john_2001 = Player("doe", "john", 2001)

tournoi_test = Tournament("Test", "taverny", 25072024, "on s'éclate en python!")

tournoi_test.add_player(blunt_roger_1982)
tournoi_test.add_player(doe_john_2001)

print(str(tournoi_test))

blunt_roger_1982.add_national_chess_number("AB12345")

print(blunt_roger_1982.national_chess_number)

round1 = Turn("round1")

tournoi_test.add_turn(round1)

print(str(tournoi_test))

match1 = Match(doe_john_2001, blunt_roger_1982)

round1.add_match(match1)

print("\nMatches in Round 1:")
for match in round1.matches:
    print(f"{match.player1.first_name} {match.player1.family_name} vs {match.player2.first_name} {match.player2.family_name}")

match1.match_result(blunt_roger_1982)

print(str(doe_john_2001))

print(str(blunt_roger_1982))
