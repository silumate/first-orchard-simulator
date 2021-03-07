import random


class Player:
    def __init__(self, game):
        self.game = game

    def move(self):
        """
        Randomly choose a legal move
        :return:
        """

        choices = []
        if self.game.green_apples > 0:
            choices.append(self.game.move_green)
        if self.game.red_apples > 0:
            choices.append(self.game.move_red)
        if self.game.blue_plums > 0:
            choices.append(self.game.move_blue)
        if self.game.yellow_pears > 0:
            choices.append(self.game.move_yellow)

        random_index = random.randint(0, len(choices) - 1)
        f = choices[random_index]
        f(True)
