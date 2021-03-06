import random

from FirstOrchard.Game import Game


class GameOptimalWithoutBias(Game):

    def move_strategically(self):
        m = max(self.green_apples, self.red_apples, self.blue_plums, self.yellow_pears)
        choices = []
        if self.green_apples >= m: choices.append(self.move_green)
        if self.red_apples >= m:   choices.append(self.move_red)
        if self.blue_plums >= m:   choices.append(self.move_blue)
        if self.yellow_pears >= m: choices.append(self.move_yellow)

        random_index = random.randint(0, len(choices) - 1)
        f = choices[random_index]
        f(True)
