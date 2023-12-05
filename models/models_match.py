class Match:
    """
    Match class
    """
    def __init__(self, player1, score1, player2, score2):
        self.players = ([player1, score1], [player2, score2])
        self.result = None

    def record_result(self):
        """
        Function recording the score of the players in the current match
        """
        while True:
            self.result = input(
                f"Enter the result for {self.players[0][0].first_name} {self.players[0][0].last_name} vs."
                f" {self.players[1][0].first_name} {self.players[1][0].last_name} \n"
                f"The winner is: 1 for {self.players[0][0].first_name}, 2 for {self.players[1][0].first_name}, "
                f"0 for a draw: ")

            if self.result in ('1', '2', '0'):
                if self.result == '1':
                    self.players[0][0].is_winner()
                elif self.result == '2':
                    self.players[1][0].is_winner()
                elif self.result == '0':
                    self.players[0][0].is_draw()
                    self.players[1][0].is_draw()

                for player, score in self.players:
                    player.score += score

                break
            else:
                print("Invalid input. Please enter 1, 2, or 0.")
