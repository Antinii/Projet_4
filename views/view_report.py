import json

FILENAME = "./data/completed_tournaments.json"


class ViewReport:

    @staticmethod
    def get_players_from_selected_tournament():
        try:
            with open(FILENAME, 'r') as file:
                completed_tournaments = json.load(file)
        except FileNotFoundError:
            print(f"File '{FILENAME}' not found.")
            return []

        print("Completed Tournaments:")
        for i, tournament in enumerate(completed_tournaments, start=1):
            print(f"{i}. {tournament['name']}")

        selected_tournament = input("Enter the tournament number to view the players: ")
        try:
            selected_index = int(selected_tournament) - 1
            if 0 <= selected_index < len(completed_tournaments):
                players = completed_tournaments[selected_index].get('players', [])
                sorted_players = sorted(players, key=lambda x: x['last_name'])
                print("\nList of all the players in the selected tournament")
                for player in sorted_players:
                    print(f"- {player['first_name']} {player['last_name']}")
                return sorted_players
            else:
                print("Invalid tournament number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

        return []

    @staticmethod
    def get_rounds_and_matches():
        try:
            with open(FILENAME, 'r') as file:
                completed_tournaments = json.load(file)
        except FileNotFoundError:
            print(f"File '{FILENAME}' not found.")
            return

        print("Completed Tournaments:")
        for i, tournament in enumerate(completed_tournaments, start=1):
            print(f"{i}. {tournament['name']} ({tournament['date']})")

        selected_index = input("Enter the number of the tournament to view rounds and matches: ")
        try:
            selected_tournament = completed_tournaments[int(selected_index) - 1]
            for round_num, matches in selected_tournament.items():
                if round_num.startswith('Round'):
                    print(f"\n{round_num}:")
                    for match in matches['matches']:
                        player1_name = match['player1']['name']
                        player2_name = match['player2']['name']
                        result = match['result']
                        if result == '1':
                            result_str = f"{player1_name} wins"
                        elif result == '2':
                            result_str = f"{player2_name} wins"
                        elif result == '0':
                            result_str = "Draw"
                        else:
                            result_str = "Invalid result"

                        print(f"{player1_name} vs. {player2_name}, Result: {result_str}")

            players = selected_tournament['players']
            leaderboard = sorted(players, key=lambda player: player['score'], reverse=True)

            print(f"\nLeaderboard for {selected_tournament['name']}:\n")
            for index, player in enumerate(leaderboard, start=1):
                print(f"{index}. {player['first_name']} {player['last_name']} - Score: {player['score']}")

        except (IndexError, ValueError):
            print("Invalid input or tournament number.")
