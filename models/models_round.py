from datetime import datetime


class Round:
    ROUND_NUMBER = 1

    def __init__(self):
        self.name = f"Round {Round.ROUND_NUMBER}"
        Round.ROUND_NUMBER += 1
        self.start_time = datetime.now()
        self.start_time = self.start_time.replace(microsecond=0)
        self.end_time = None
        self.matches = []

        print(f"{self.name} started at {self.start_time}")
        print(f"{self.name} matches: \n")

    # Fonction ajoutant le match en cours à la liste des matchs du round
    def add_match(self, match):
        self.matches.append(match)

    # Fonction terminant le round en donnant la date et l'heure de fin
    def end_round(self):
        self.end_time = datetime.now()
        self.end_time = self.end_time.replace(microsecond=0)
        print(f"\n{self.name} ended at {self.end_time}")
