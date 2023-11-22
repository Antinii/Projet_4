class ViewTournament:

    @staticmethod
    def get_name():
        while True:
            name = input("Enter the name of the tournament: ")
            return name

    @staticmethod
    def get_location():
        while True:
            location = input("Enter the location of the tournament: ")
            return location

    @staticmethod
    def get_date():
        while True:
            date = input("Enter the date of the tournament: ")
            return date

    @staticmethod
    def get_num_rounds():
        rounds = input("Enter the number of rounds in the tournament (default is 4): ")
        if not rounds.isdigit():
            rounds = 4
        else:
            rounds = int(rounds)
        return rounds

    @staticmethod
    def get_description():
        while True:
            description = input("Enter the description of the tournament: ")
            if len(description) <= 50:
                return description
            else:
                print("Your description is too long !")

    @staticmethod
    def select_tournament(tournaments):
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
