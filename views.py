from models import Player, Tournament, Turn, Match, TournamentList


def display_player_info(self):
    return (f"{self.family_name} {self.first_name}, "
            f"date of birth: {self.date_of_birth}, "
            f"ID: {self.national_chess_number}, "
            f"points: {self.points}")


def display_tournament_list():
    print(TournamentList)


def display_tournament_info(self):
    return f"{self.name}, {self.date}"


def display_tournament_players_info(tournament):
    Tournament.players_list.sort(key=lambda player: (player.family_name, player.first_name))
    for player in Tournament.players_list:
        print(f"{player.family_name} {player.first_name}")


def display_tournament_turns(self):
    print(self.turns_list)


def display_turn_matches(self):
    print(self.matches)
