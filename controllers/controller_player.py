from Scripts.views.view_player import ViewPlayer
from Scripts.models.models_player import Player

import json

FILENAME = "./data/players.json"


class ControllerPlayer:
    def __init__(self):
        self.view_player = ViewPlayer()

    # Fonction permettant la création d'un joueur dans la base de données
    def create_player(self):
        player_data = {}
        with open(FILENAME, "r") as f:
            temp = json.load(f)
        player_data["first_name"] = self.view_player.get_first_name()
        player_data["last_name"] = self.view_player.get_last_name()
        player_data["date_of_birth"] = self.view_player.get_date_of_birth()
        player_data["national_chess_id"] = self.view_player.get_national_chess_id()
        temp.append(player_data)
        with open(FILENAME, "w") as f:
            json.dump(temp, f, indent=4)

    # Fonction permettant l'affichage des joueurs trié par ordre alphabétique
    def view_players(self):
        with open(FILENAME, "r") as f:
            temp = json.load(f)
            temp.sort(key=lambda player: player["last_name"])
            print("\nList of all players in alphabetical order: \n")
            for entry in temp:
                first_name = entry["first_name"]
                last_name = entry["last_name"]
                date_of_birth = entry["date_of_birth"]
                chess_id = entry["national_chess_id"]
                print(f"Name : {last_name} {first_name}")
                print(f"Birthday : {date_of_birth}")
                print(f"National chess ID : {chess_id}\n")

    @classmethod
    def load_players(cls, player_config):
        players = []
        try:
            with open(player_config, "r") as file:
                player_data = json.load(file)
                players = [cls.from_dict(player) for player in player_data]
        except FileNotFoundError:
            print(f"Config file '{player_config}' not found. Exiting.")
            exit()
        return players

    @classmethod
    def from_dict(cls, player_data):
        return Player(
            player_data["first_name"],
            player_data["last_name"],
            player_data["date_of_birth"],
            player_data["national_chess_id"],
        )
