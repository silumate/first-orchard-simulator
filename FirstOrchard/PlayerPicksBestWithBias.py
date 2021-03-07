from FirstOrchard.Player import Player


class PlayerPicksBestWithBias(Player):

    def move(self):
        """
        find a color with the max count.  Always pick the same colors first if more than one have the max.
        :return:
            None
        """
        # this is biased because it will always try to move green first then red, blue yellow
        m = max(self.game.green_apples, self.game.red_apples, self.game.blue_plums, self.game.yellow_pears)
        if self.game.green_apples >= m:
            self.game.move_green(True)
        elif self.game.red_apples >= m:
            self.game.move_red(True)
        elif self.game.blue_plums >= m:
            self.game.move_blue(True)
        elif self.game.yellow_pears >= m:
            self.game.move_yellow(True)
