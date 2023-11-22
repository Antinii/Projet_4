class ViewPlayer:

    @staticmethod
    def get_last_name():
        while True:
            last_name = input("Enter the last name: ")
            return last_name

    @staticmethod
    def get_first_name():
        while True:
            first_name = input("Enter the first name: ")
            return first_name

    @staticmethod
    def get_date_of_birth():
        while True:
            date_of_birth = input("Enter the date of birth: ")
            return date_of_birth

    @staticmethod
    def get_national_chess_id():
        while True:
            national_chess_id = input("Enter the national chess ID (as \"AB12345\": ")
            return national_chess_id

    @staticmethod
    def select_players(players):
        selected_players = []

        while True:
            print("Available players for the tournament:")
            for i, player in enumerate(players, start=1):
                print(f"{i}. {player.first_name} {player.last_name} {player.national_chess_id}")

            choice = input("Enter the player number to register for the tournament (or type "
                           "'done' to finish selecting): ")

            if choice.lower() == 'done':
                if not selected_players:
                    print("No players selected. Please select at least one player.")
                    continue
                else:
                    return selected_players

            try:
                player_index = int(choice) - 1
                if 0 <= player_index < len(players):
                    selected_player = players[player_index]
                    if selected_player not in selected_players:
                        selected_players.append(selected_player)
                        print(f"Player registered: {selected_player.first_name} {selected_player.last_name}\n")
                    else:
                        print("Player already selected. Choose a different player.")
                else:
                    print("Invalid player number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid player number.")
