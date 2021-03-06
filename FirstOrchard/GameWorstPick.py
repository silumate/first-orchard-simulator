
from FirstOrchard.Game import Game


class GameWorstPick(Game):

    def move_strategically(self):
        # find first color with lowest count above zero
        for i in range(1, 5):
            if self.green_apples == i:
                self.move_green(True)
                return
            if self.red_apples == i:
                self.move_red(True)
                return
            if self.blue_plums == i:
                self.move_blue(True)
                return
            if self.yellow_pears == i:
                self.move_yellow(True)
                return
        raise Exception("shouldn't get here!")
