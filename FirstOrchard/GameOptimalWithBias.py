
from FirstOrchard.Game import Game


class GameOptimalBiased(Game):

    def move_strategically(self):
        # this is biased because it will always try to move green first then red, blue yellow
        m = max(self.green_apples, self.red_apples, self.blue_plums, self.yellow_pears)
        if self.green_apples >= m:
            self.move_green(True)
        elif self.red_apples >= m:
            self.move_red(True)
        elif self.blue_plums >= m:
            self.move_blue(True)
        elif self.yellow_pears >= m:
            self.move_yellow(True)
