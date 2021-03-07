from FirstOrchard.Player import Player
import random


class PlayerPicksBestWithoutBias(Player):

    def move(self):
        """
        find all color with the max count.  Randomly pick one.
        :return:
            None
        """
        m = max(self.game.green_apples, self.game.red_apples, self.game.blue_plums, self.game.yellow_pears)
        choices = []
        if self.game.green_apples >= m: choices.append(self.game.move_green)
        if self.game.red_apples >= m:   choices.append(self.game.move_red)
        if self.game.blue_plums >= m:   choices.append(self.game.move_blue)
        if self.game.yellow_pears >= m: choices.append(self.game.move_yellow)

        random_index = random.randint(0, len(choices) - 1)
        f = choices[random_index]
        f(True)
