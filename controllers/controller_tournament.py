import json
import random

from models.models_match import Match
from models.models_player import Player
from models.models_round import Round
from models.models_tournament import Tournament
from views.base import MainMenu
from views.view_player import ViewPlayer
from views.view_tournament import ViewTournament
from controllers.controller_player import ControllerPlayer

FILENAME = "./data/tournaments.json"


class ControllerTournament:
    """
    Tournament controller class
    """

    def __init__(self):
        self.view_tournament = ViewTournament()
        self.view_player = ViewPlayer()
        self.base = MainMenu()
        self.controller_player = ControllerPlayer()

    def create_tournament(self):
        """
        Function saving a tournament in the json
        """
        tournament_data = {}
        with open(FILENAME, "r") as f:
            temp = json.load(f)
        tournament_data["name"] = self.view_tournament.get_name()
        tournament_data["location"] = self.view_tournament.get_location()
        tournament_data["date"] = self.view_tournament.get_date()
        tournament_data["num_rounds"] = self.view_tournament.get_num_rounds()
        tournament_data["description"] = self.view_tournament.get_description()
        temp.append(tournament_data)
        with open(FILENAME, "w") as f:
            json.dump(temp, f, indent=4)

    def view_tournaments(self):
        """
        Function showing the list of all tournaments
        """
        with open(FILENAME, "r") as f:
            temp = json.load(f)
            print("\nList of all tournaments: \n")
            for entry in temp:
                name = entry["name"]
                location = entry["location"]
                date = entry["date"]
                print(f"- {name} ({date}) {location}")

    @classmethod
    def load_tournaments(cls, tournament_config):
        """
        Loading all the tournaments from the json
        :param tournament_config:
        """
        tournaments = []
        try:
            with open(tournament_config, "r") as file:
                tournament_data = json.load(file)
                tournaments = [
                    cls.from_dict(tournament) for tournament in tournament_data
                ]
        except FileNotFoundError:
            print(f"Config file '{tournament_config}' not found. Exiting.")
            exit()
        return tournaments

    @classmethod
    def from_dict(cls, tournament_data):
        return Tournament(
            tournament_data["name"],
            tournament_data["location"],
            tournament_data["date"],
            tournament_data["description"],
            tournament_data["num_rounds"],
        )

    def launch_tournament(self):
        """
        Function launching a tournament from the start
        """
        selected_tournament, selected_players = self.setup_tournament()

        print(f'\nTournament "{selected_tournament.name}" started !\n')
        for round_number in range(1, selected_tournament.num_rounds + 1):
            self.start_round(selected_tournament, round_number, selected_players)

        selected_tournament.save_tournament_to_json("./data/completed_tournaments.json")
        with open('./data/pending_tournament.json', 'w') as file:
            json.dump({}, file)

    def setup_tournament(self):
        """
        Function setting up the tournament by loading the list of tournaments
        and the list of players, and registering them all.
        """
        tournaments = self.load_tournaments("./data/tournaments.json")
        selected_tournament = self.view_tournament.select_tournament(tournaments)

        players = self.controller_player.load_players("./data/players.json")
        selected_players = self.view_player.select_players(players)

        selected_tournament.players = selected_players
        self.tournament = selected_tournament
        return selected_tournament, selected_players

    def start_round(self, selected_tournament, round_number, selected_players):
        """
        Function starting a round in the tournament
        :param selected_tournament:
        :param round_number:
        :param selected_players:
        """
        current_round = Round()
        selected_tournament.rounds.append(current_round)

        if round_number == 1:
            random.shuffle(selected_players)

        pairings = self.generate_pairings(selected_players)
        self.play_round_matches(current_round, pairings)

        self.display_scoreboard(selected_players)
        print("\n")

        self.save_tournament_state(selected_tournament)

    def play_round_matches(self, current_round, pairings):
        """
        Function playing all the matches available in a round
        :param current_round:
        :param pairings:
        """
        for i, (player1, player2) in enumerate(pairings):
            print(f"Match {i + 1}: {player1.first_name} vs. {player2.first_name}")
        print("\n")
        for i, (player1, player2) in enumerate(pairings):
            self.save_tournament_state(self.tournament)
            match = Match(player1, 0, player2, 0)
            match.record_result()
            current_round.add_match(match)

        current_round.end_round()

    def generate_pairings(self, selected_players):
        """
        Function generating a pair of players to play a match
        :param selected_players
        :return: a pair of players
        """
        if not hasattr(self, "pairings_record"):
            self.pairings_record = set()
        if self.tournament.rounds == 1:
            random.shuffle(selected_players)
            pairings = [(selected_players[i], selected_players[i + 1]) for i in range(0, len(selected_players), 2)]
        else:
            pairings = []
            selected_players.sort(key=lambda player: player.score, reverse=True)
            used_players = set()
            already_paired = set()

            for i in range(0, len(selected_players) - 1, 2):
                player1 = selected_players[i]
                player2 = selected_players[i + 1]
                while (player1, player2) in self.pairings_record or (player2, player1) in self.pairings_record or \
                        (player1, player2) in already_paired or (player2, player1) in already_paired:
                    i += 1
                    if i + 1 >= len(selected_players):
                        break
                    player1 = selected_players[i]
                    player2 = selected_players[i + 1]

                pairings.append((player1, player2))
                self.pairings_record.add((player1, player2))
                self.pairings_record.add((player2, player1))
                used_players.add(player1)
                used_players.add(player2)
                already_paired.add((player1, player2))
                already_paired.add((player2, player1))

            if len(selected_players) % 2 != 0:
                remaining_player = selected_players[-1]
                opponent = None
                for player in selected_players[::-1]:
                    if player not in used_players:
                        opponent = player
                        break

                if (opponent is not None and (remaining_player, opponent) not in self.pairings_record
                        and (opponent, remaining_player) not in self.pairings_record
                        and (remaining_player, opponent) not in already_paired
                        and (opponent, remaining_player) not in already_paired):
                    pairings.append((remaining_player, opponent))
                    self.pairings_record.add((remaining_player, opponent))
                    self.pairings_record.add((opponent, remaining_player))
                    already_paired.add((remaining_player, opponent))
                    already_paired.add((opponent, remaining_player))

        return pairings

    def display_scoreboard(self, selected_players):
        """
        Function displaying the scoreboard at the end of a round
        :param selected_players:
        """
        print("\nRound points:")
        selected_players.sort(key=lambda player: player.score, reverse=True)
        for i, player in enumerate(selected_players, start=1):
            print(f"{i}. {player.first_name} {player.last_name}: {player.score} points ")

    def save_tournament_state(self, tournament):
        """
        Function to save the tournament state to the pending_tournament json file
        :param tournament: The tournament object whose state will be saved
        """
        tournament_data = {
            "name": tournament.name,
            "location": tournament.location,
            "date": tournament.date,
            "description": tournament.description,
            "num_rounds": tournament.num_rounds,
            "players": [],
        }

        for player in tournament.players:
            player_info = {
                "first_name": player.first_name,
                "last_name": player.last_name,
                "date_of_birth": player.date_of_birth,
                "chess_id": player.national_chess_id,
                "score": player.score
            }
            tournament_data["players"].append(player_info)

        for index, round_data in enumerate(self.tournament.rounds, start=1):
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

        with open("./data/pending_tournament.json", "w") as file:
            json.dump(tournament_data, file, indent=4)

    def continue_tournament(self):
        """
        Function loading the data from the pending tournament json file
        and continuing the tournament at his state
        :return: the selected tournament
        """
        try:
            with open('./data/pending_tournament.json', 'r') as file:
                tournament_data = json.load(file)
        except FileNotFoundError:
            print("\nNo pending tournament found.")
            return

        if not tournament_data:
            print("\nNo pending tournament found.")
            return

        tournament_name = tournament_data['name']
        tournament_location = tournament_data['location']
        tournament_date = tournament_data['date']
        tournament_description = tournament_data['description']
        tournament_num_rounds = tournament_data['num_rounds']
        players_data = tournament_data['players']

        players = [
            Player(player['first_name'], player['last_name'], player['date_of_birth'], player['chess_id'],)
            for player in players_data
        ]

        tournament = Tournament(tournament_name, tournament_location, tournament_date, tournament_description,
                                tournament_num_rounds)
        tournament.players = players

        selected_tournament = tournament
        self.tournament = selected_tournament
        selected_players = players

        print(f'\nTournament "{selected_tournament.name}" continued !\n')
        for round_number in range(1, selected_tournament.num_rounds + 1):
            self.start_round(selected_tournament, round_number, selected_players)

        selected_tournament.save_tournament_to_json("./data/completed_tournaments.json")
        with open('./data/pending_tournament.json', 'w') as file:
            json.dump({}, file)

        return selected_tournament
