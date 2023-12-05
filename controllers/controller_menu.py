import sys

from controllers.controller_player import ControllerPlayer
from controllers.controller_tournament import ControllerTournament
from views.base import MainMenu
from views.view_report import ViewReport


class ControllerMenu:
    """
    Menu controller class
    """
    def __init__(self):
        pass

    def home_menu(self):
        """
        Function managing the main menu
        """
        while True:
            home = MainMenu()
            home.display_main_menu()
            choice = input("Select 1, 2, 3 or 4 : ")

            if choice == "1":
                self.tournament_menu()

            elif choice == "2":
                self.player_menu()

            elif choice == "3":
                self.report_menu()

            elif choice == "4":
                print("Exiting the program...")
                sys.exit()

            else:
                print("You must select 1, 2, 3 or 4")

    def tournament_menu(self):
        """
        Function managing the tournament menu
        """
        while True:
            tournament_menu = MainMenu()
            tournament_menu.display_tournaments_menu()
            choice = input("Select 1, 2, 3 or 4 : ")

            if choice == "1":
                tournament = ControllerTournament()
                tournament.create_tournament()

            elif choice == "2":
                tournament = ControllerTournament()
                tournament.launch_tournament()

            elif choice == "3":
                tournament = ControllerTournament()
                tournament.continue_tournament()

            elif choice == "4":
                self.home_menu()

            else:
                print("You must select 1, 2, 3 or 4")

    def player_menu(self):
        """
        Function managing the player menu
        """
        while True:
            tournament_menu = MainMenu()
            tournament_menu.display_players_menu()
            choice = input("Select 1, 2 or 3: ")

            if choice == "1":
                add_player = ControllerPlayer()
                add_player.create_player()

            elif choice == "2":
                view_players = ControllerPlayer()
                view_players.view_players()

            elif choice == "3":
                self.home_menu()

            else:
                print("You must select 1, 2 or 3")

    def report_menu(self):
        """
        Function managing the reports menu
        """
        while True:
            report_menu = MainMenu()
            report_menu.display_reports_menu()
            choice = input("Select 1, 2, 3, 4, 5 or 6: ")

            if choice == "1":
                all_players_list = ControllerPlayer()
                all_players_list.view_players()

            elif choice == "2":
                all_tournaments_list = ControllerTournament()
                all_tournaments_list.view_tournaments()

            elif choice == "3":
                tournament_players = ViewReport()
                tournament_players.get_players_from_selected_tournament()

            elif choice == "4":
                rounds_matches = ViewReport()
                rounds_matches.get_rounds_and_matches()

            elif choice == "5":
                self.home_menu()

            else:
                print("You must select 1, 2, 3, 4, 5 or 6")
