from models import Player, Tournament, Turn, Match, TournamentList


def update_points(self, points):
    self.points += points


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
