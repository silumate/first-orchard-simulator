from FirstOrchard.Player import Player


class PlayerPicksWorst(Player):

    def move(self):
        """
        find the resources with the lowest count, but above zero, and move that to the basket.
        :return:
            None
        """
        # Start with a count of 1, look for a color that has it, if not, iterate with a count of 2...
        for i in range(1, 5):
            if self.game.green_apples == i:
                self.game.move_green(True)
                return
            if self.game.red_apples == i:
                self.game.move_red(True)
                return
            if self.game.blue_plums == i:
                self.game.move_blue(True)
                return
            if self.game.yellow_pears == i:
                self.game.move_yellow(True)
                return
        raise Exception("shouldn't get here!")
