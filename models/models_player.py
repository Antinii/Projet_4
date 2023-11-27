class Player:

    def __init__(self, first_name, last_name, date_of_birth, national_chess_id):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.national_chess_id = national_chess_id
        self.score = 0

    def __str__(self):
        return f"{self.last_name} {self.first_name} Score: {self.score}"

    # Fonction ajoutant 1 au score du joueur s'il a gagné le match
    def is_winner(self):
        self.score += 1

    # Fonction ajoutant 0.5 au score des joueurs si il y a match nul
    def is_draw(self):
        self.score += 0.5
