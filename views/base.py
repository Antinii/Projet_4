class MainMenu:
    """
    Main menu class
    """

    @staticmethod
    def display_main_menu():
        """
        Function printing the main menu options
        """
        print("------------------------------\n"
              "   CHESS TOURNAMENT PROGRAM \n"
              "------------------------------")
        print("[1]. Tournaments management")
        print("[2]. Players management")
        print("[3]. Reports management")
        print("[4]. Exit the program")

    @staticmethod
    def display_players_menu():
        """
        Function printing the players menu options
        """
        print("------------------------------\n"
              "      PLAYERS MANAGEMENT \n"
              "------------------------------")
        print("[1]. Create a new player")
        print("[2]. Show a list of all players")
        print("[3]. Return back to main menu")

    @staticmethod
    def display_tournaments_menu():
        """
        Function printing the tournament menu options
        """
        print("------------------------------\n"
              "    TOURNAMENTS MANAGEMENT \n"
              "------------------------------")
        print("[1]. Create a new tournament")
        print("[2]. Launch a new tournament")
        print("[3]. Continue a pending tournament")
        print("[4]. Return back to main menu")

    @staticmethod
    def display_reports_menu():
        """
        Function printing the reports menu options
        """
        print("------------------------------\n"
              "      REPORTS MANAGEMENT \n"
              "------------------------------")
        print("[1]. List of all players in the database")
        print("[2]. List of all tournaments in the database")
        print("[3]. List of all players in a specific tournament")
        print("[4]. List of all the rounds and matches of a specific tournament")
        print("[5]. Return back to main menu")
