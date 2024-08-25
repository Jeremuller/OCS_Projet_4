from views import TournamentView
from models import Tournament, Player
import json
import os


class TournamentController:

    def __init__(self):
        self.view = TournamentView()
        self.tournament = None

    def start(self):

        TournamentView.display_welcome_message()

        while True:
            main_menu_choice = TournamentView.display_menu()

            if main_menu_choice == "1":
                self.create_tournament()
            elif main_menu_choice == "2":
                self.add_player()
            elif main_menu_choice == "3":
                self.run_tournament()
            elif main_menu_choice == "4":
                TournamentView.display_informations_menu()
            elif main_menu_choice == "5":
                print("Au revoir!")
                break
            else:
                print("Choix invalide, veuillez entre le chiffre correspondant à votre requête")

    def tournament_in_progress(self):
        return self.tournament is not None

    def create_tournament(self):
        if self.tournament_in_progress():
            print("Un tournoi est déjà en cours. Veuillez le terminer ou l'annuler d'abord.")

        name, location, date, description = TournamentView.get_tournament_informations()
        self.tournament = Tournament(name, location, date, description)
        TournamentView.display_tournament_infos(self.tournament)

    def add_player(self):
        if self.tournament_in_progress():
            family_name, first_name, date_of_birth = TournamentView.get_player_informations()
            player = Player(family_name, first_name, date_of_birth, points=0)
            self.tournament.add_player(player)
            TournamentView.display_players(self.tournament.players_list)
        else:
            print("Il n'y a pas de tournoi en cours")

    def run_tournament(self):
        # On vérifie d'abord qu'un tournoi a été crée et qu'il comporte des joueurs
        if self.tournament_in_progress():
            if not self.tournament.players_list:
                print("Le tournoi n'a aucun joueur!")
                return

            # Contrôle que le tournoi n'est pas encore terminé
            while self.tournament.actual_turn_number < self.tournament.number_of_turns:
                print(f"Début du tour {self.tournament.actual_turn_number + 1}/{self.tournament.number_of_turns}")

                # Générer les matchs
                turn = self.tournament.create_turn(f"round_{self.tournament.actual_turn_number + 1}")
                matches = turn.generate_matches()

                # Saisie des résultats des matchs
                self.process_match_results(matches)

                # Demander à l'utilisateur s'il souhaite continuer
                while True:
                    continue_choice = input("Souhaitez vous passer au tour suivant ? (oui/non): ").lower()
                    if continue_choice == "non":
                        confirm_exit = input("Êtes vous sûr de vouloir quitter le tournoi? "
                                             "Cela supprimera le tournoi en cours. (oui/non): ").lower()
                        if confirm_exit == "oui":
                            print("Tournoi interrompu")
                            return
                        else:
                            print("Retour au tournoi.")
                            break
                    elif continue_choice == "oui":
                        self.tournament.actual_turn_number += 1
                        break
                    else:
                        print("Choix invalide, veuillez entrer \"oui\" ou \"non\".")

            # Message de fin de tournoi avec affichage des participants et leurs scores
            print("\nTournoi terminé! Voici le récapitulatif des scores: ")
            sorted_players = sorted(self.tournament.players_list, key=lambda player: player.points, reverse=True)
            for player in sorted_players:
                print(f"Joueur : {player.first_name} {player.family_name} - Points : {player.points}")

    def informations_menu(self):
        while True:
            informations_menu_choice = TournamentView.display_menu()

            if informations_menu_choice == "1":
                if self.tournament_in_progress():
                    TournamentView.display_tournament_infos(self.tournament)
                else:
                    print("Il n'y a aucun tournoi en cours.")
            elif informations_menu_choice == "2":
                if self.tournament_in_progress():
                    TournamentView.display_players(self.tournament)
                else:
                    print("Il n'y a aucun tournoi en cours.")
            elif informations_menu_choice == "3":
                if self.tournament_in_progress():
                    TournamentView.display_tournament_turns(self.tournament)
                else:
                    print("Il n'y a aucun tournoi en cours.")
            elif informations_menu_choice == "4":
                print("cette partie est en cours de développement")
                pass
                # ajouter une liaison vers les joueurs enregistrés
            elif informations_menu_choice == "5":
                print("cette partie est en cours de développement")
                pass
                # ajouter une liaison vers les tournois archivés
            elif informations_menu_choice == "6":
                break
            else:
                print("Choix invalide, veuillez entre le chiffre correspondant à votre requête")

    def process_match_results(self, matches):
        for match in matches:
            score_player1, score_player2 = TournamentView.get_match_results(match)
            match.update_players_points(score_player1, score_player2)


class InformationController:

    @staticmethod
    def display_sorted_players():
        loaded_data = Player.load_from_json(file_path="test.json")

        if not isinstance(loaded_data, list):
            raise TypeError("Loaded data should be a list of dictionaries.")

        players_list = [Player.deserialize_from_dict(data) for data in loaded_data]

        sorted_players_list = sorted(players_list, key=lambda player: player.family_name)

        TournamentView.display_players(sorted_players_list)

    @staticmethod
    def display_archived_tournaments():
        tournaments = Tournament.load_archived_tournaments()
        if not tournaments:
            print("Aucun tournoi archivé n'a été trouvé")
            return

        print("\n -- Liste des tournois archivés --")
        for i, tournament in enumerate(tournaments, start=1):
            print(f"{i}. {tournament.name} - Date: {tournament.date}")


def integration_test():

    players_list = [
        Player(first_name="Magnus", family_name="Carlsen", date_of_birth="30111990"),
        Player(first_name="Hikaru", family_name="Nakamura", date_of_birth="09121987"),
        Player(first_name="Fabiano", family_name="Caruana", date_of_birth="30111992"),
        Player(first_name="Ian", family_name="Nepomniachtchi", date_of_birth="14071990")
    ]

    players_list[0].national_chess_number = "NOR19901130"
    players_list[1].national_chess_number = "USA19871209"
    players_list[2].national_chess_number = "USA19921130"
    players_list[3].national_chess_number = "RUS19900714"

    print("Initial list of players:")
    print(str(players_list))

    tournament = Tournament(
        name="Grand chess Tournament",
        location="Paris",
        date="25082024",
        description="2024's edition Grand Chess Tournament"
    )

    for player in players_list:
        tournament.add_player(player)

    first_turn = tournament.create_turn("Round_1")
    first_turn.generate_matches()

    print("\nInitial tournament data:")
    print(tournament)

    test_file = "tournament_test.json"
    tournament.save_to_json(test_file)

    loaded_data = Tournament.load_from_json(test_file)
    deserialized_tournament = Tournament.deserialize_from_dict(loaded_data)

    print("\nDesrialized tournament data:")
    print(deserialized_tournament)

    # data compare
    print("\nComparaison des joueurs avant et après la déserialisation:")
    for original_player, deserialized_player in zip(tournament.turns_list, deserialized_tournament.turns_list):
        print(f"Avant: {original_player}")
        print(f"Après: {deserialized_player}")
        print()

    print("\nComparaison des tours avant et après désérialisation:")
    for original_turn, deserialized_turn in zip(tournament.turns_list, deserialized_tournament.turns_list):
        print(f"Avant: {original_turn}")
        print(f"Après: {deserialized_turn}")
        print()

    os.remove("tournament_test.json")

    print("test réussi")

integration_test()


"""@classmethod
def test_archived_tournaments():
    tournois = [
        Tournament(name="Open Hiver", date="25122023", location="Paris", description="youhou"),
        Tournament(name="Open Summer", date="21062024", location="Paris", description="youhou"),
        Tournament(name="Open Spring", date="21032024", location="Paris", description="youhou")
    ]

    for tournoi in tournois:
        tournoi."""

# Point d'entrée du programme
if __name__ == "__main__":
    controller = TournamentController()
    controller.start()
