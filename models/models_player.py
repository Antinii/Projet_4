class Player:
    """
    Player class
    """
    def __init__(self, first_name, last_name, date_of_birth, national_chess_id):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.national_chess_id = national_chess_id
        self.score = 0

    def is_winner(self):
        """
        Function updating the score of the winner by 1
        """
        self.score += 1

    def is_draw(self):
        """
        Function updating the score of the players for a draw by giving them each 0.5 points
        """
        self.score += 0.5
