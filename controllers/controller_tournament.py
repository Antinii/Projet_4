from Scripts.views.view_tournament import ViewTournament
from Scripts.views.view_player import ViewPlayer
from Scripts.models.models_tournament import Tournament
from Scripts.controllers.controller_player import ControllerPlayer
from Scripts.models.models_round import Round
from Scripts.models.models_match import Match
from Scripts.views.base import MainMenu

import json
import random


FILENAME = "./data/tournaments.json"


class ControllerTournament:
    def __init__(self):
        self.view_tournament = ViewTournament()
        self.view_player = ViewPlayer()
        self.base = MainMenu()
        self.controller_player = ControllerPlayer()

    def create_tournament(self):
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
        tournaments = []
        try:
            with open(tournament_config, "r") as file:
                tournament_data = json.load(file)
                tournaments = [cls.from_dict(tournament) for tournament in tournament_data]
        except FileNotFoundError:
            print(f"Config file '{tournament_config}' not found. Exiting.")
            exit()
        return tournaments

    @classmethod
    def from_dict(cls, tournament_data):
        return Tournament(
            tournament_data['name'],
            tournament_data['location'],
            tournament_data['date'],
            tournament_data['description'],
            tournament_data['num_rounds']
        )

    def launch_tournament(self):
        selected_tournament, selected_players = self.setup_tournament()

        print(f"\nTournament \"{selected_tournament.name}\" started !\n")
        for round_number in range(1, selected_tournament.num_rounds + 1):
            self.start_round(selected_tournament, round_number, selected_players)

        selected_tournament.save_tournament_to_json('./data/completed_tournaments.json')

    def setup_tournament(self):
        tournaments = self.load_tournaments("./data/tournaments.json")
        selected_tournament = self.view_tournament.select_tournament(tournaments)

        players = self.controller_player.load_players("./data/players.json")
        selected_players = self.view_player.select_players(players)

        selected_tournament.players = selected_players
        self.tournament = selected_tournament
        return selected_tournament, selected_players

    def start_round(self, selected_tournament, round_number, selected_players):
        current_round = Round()
        selected_tournament.rounds.append(current_round)

        if round_number == 1:
            random.shuffle(selected_players)

        pairings = self.generate_pairings(selected_players)
        self.play_round_matches(current_round, pairings)

        self.display_scoreboard(selected_players)
        print("\n")

    def play_round_matches(self, current_round, pairings):
        for i, (player1, player2) in enumerate(pairings):
            print(f"Match {i + 1}: {player1.first_name} vs. {player2.first_name}")
        print("\n")
        for i, (player1, player2) in enumerate(pairings):
            match = Match(player1, 0, player2, 0)
            match.record_result()
            current_round.add_match(match)
        current_round.end_round()

    def generate_pairings(self, selected_players):
        if not hasattr(self, 'pairings_record'):
            self.pairings_record = set()

        if self.tournament.rounds == 1:
            random.shuffle(selected_players)
            pairings = [(selected_players[i], selected_players[i + 1]) for i in range(0, len(selected_players), 2)]
        else:
            pairings = []
            selected_players.sort(key=lambda player: player.score, reverse=True)

            used_players = set()
            for i in range(0, len(selected_players) - 1, 2):
                player1 = selected_players[i]
                player2 = selected_players[i + 1]

                if (player1, player2) in self.pairings_record or (player2, player1) in self.pairings_record:
                    while (player1, player2) in self.pairings_record or (player2, player1) in self.pairings_record:
                        i += 1
                        if i + 1 >= len(selected_players):
                            break
                        player1 = selected_players[i]
                        player2 = selected_players[i + 1]

                if i + 1 < len(selected_players):
                    pairings.append((player1, player2))
                    self.pairings_record.add((player1, player2))
                    self.pairings_record.add((player2, player1))
                    used_players.add(player1)
                    used_players.add(player2)

            if len(selected_players) % 2 != 0:
                remaining_player = selected_players[-1]
                opponent = None

                for player in selected_players[::-1]:
                    if player not in used_players:
                        opponent = player
                        break

                if (opponent is not None and (remaining_player, opponent) not in self.pairings_record
                        and (opponent, remaining_player) not in self.pairings_record):
                    pairings.append((remaining_player, opponent))
                    self.pairings_record.add((remaining_player, opponent))
                    self.pairings_record.add((opponent, remaining_player))

        return pairings

        # if not hasattr(self, 'pairings_record'):
        #     self.pairings_record = set()
        #
        # if self.tournament.rounds == 1:
        #     random.shuffle(selected_players)
        #     pairings = [(selected_players[i], selected_players[i + 1]) for i in range(0, len(selected_players), 2)]
        # else:
        #     pairings = []
        #     selected_players.sort(key=lambda player: player.score, reverse=True)
        #
        #     for i in range(0, len(selected_players), 2):
        #         player1 = selected_players[i]
        #         player2 = selected_players[i + 1] if i + 1 < len(selected_players) else None
        #
        #         if (player1, player2) not in self.pairings_record and (player2, player1) not in self.pairings_record:
        #             pairings.append((player1, player2))
        #             self.pairings_record.add((player1, player2))
        #             self.pairings_record.add((player2, player1))
        #
        # return pairings

    def display_scoreboard(self, selected_players):
        print("\nRound points:")
        selected_players.sort(key=lambda player: player.score, reverse=True)
        for i, player in enumerate(selected_players, start=1):
            print(f"{i}. {player.first_name} {player.last_name}: {player.score} points ")
