class PlayerPicksFavorite:

    def move(self):
        """
        Choose your favourite color first, then move down list of favourites
        :return:
            None
        """
        if self.game.blue_plums > 0:
            self.game.move_blue(True)
        elif self.game.red_apples > 0:
            self.game.move_red(True)
        elif self.game.green_apples > 0:
            self.game.move_green(True)
        elif self.game.yellow_pears > 0:
            self.game.move_yellow(True)
        else:
            raise Exception("PlayerPicksFavorite.move() can't do anything")

