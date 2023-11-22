import json


class Tournament:
    def __init__(self, name, location, date, description, num_rounds=4):
        self.name = name
        self.location = location
        self.date = date
        self.players = []
        self.rounds = []
        self.num_rounds = num_rounds
        self.description = description

    def save_tournament_to_json(self, filename):
        try:
            with open(filename, 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []

        tournament_data = {
            'name': self.name,
            'location': self.location,
            'date': self.date,
            'description': self.description,
            'number_of_rounds': self.num_rounds,
            'players': [player.__dict__ for player in self.players],
        }

        for index, round_data in enumerate(self.rounds, start=1):
            matches_data = [{
                'player1': {
                    'name': match.players[0][0].first_name,
                    'score': match.players[0][1],
                },
                'player2': {
                    'name': match.players[1][0].first_name,
                    'score': match.players[1][1],
                },
                'result': match.result,
            } for match in round_data.matches]

            tournament_data[f'Round_{index}'] = {
                'matches': matches_data
            }

        existing_data.append(tournament_data)

        with open(filename, 'w') as file:
            json.dump(existing_data, file, indent=4)
