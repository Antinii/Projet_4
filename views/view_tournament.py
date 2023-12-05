class ViewTournament:
    """
    View tournament class
    """

    @staticmethod
    def get_name():
        """
        Function asking the user to enter the name of the tournament
        :return: name of the tournament
        """
        while True:
            name = input("Enter the name of the tournament: ")
            return name

    @staticmethod
    def get_location():
        """
        Function asking the user to enter the location of the tournament
        :return: location of the tournament
        """
        while True:
            location = input("Enter the location of the tournament: ")
            return location

    @staticmethod
    def get_date():
        """
        Function asking the user to enter the date of the tournament
        :return: date of the tournament
        """
        while True:
            date = input("Enter the date of the tournament: ")
            return date

    @staticmethod
    def get_num_rounds():
        """
        Function asking the user to enter the number of rounds of the tournament
        :return: number of rounds
        """
        rounds = input("Enter the number of rounds in the tournament (default is 4): ")
        if not rounds.isdigit():
            rounds = 4
        else:
            rounds = int(rounds)
        return rounds

    @staticmethod
    def get_description():
        """
        Function asking the user to enter the description of the tournament
        :return: description of the tournament
        """
        while True:
            description = input("Enter the description of the tournament: ")
            if len(description) <= 50:
                return description
            else:
                print("Your description is too long !")

    @staticmethod
    def select_tournament(tournaments):
        """
        Function asking the user to select a tournament whitin the list of all available tournaments
        :param tournaments:
        """
        while True:
            print("\nAvailable Tournaments:")
            for i, tournament in enumerate(tournaments, start=1):
                print(f"{i}. {tournament.name} ({tournament.location}) - {tournament.date}")

            choice = input("Enter the tournament number to select (or 'exit' to quit): ")

            if choice.lower() == 'exit':
                print("Exiting program.")
                exit()

            try:
                tournament_index = int(choice) - 1
                if 0 <= tournament_index < len(tournaments):
                    return tournaments[tournament_index]
                else:
                    print("Invalid tournament number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid tournament number.")
