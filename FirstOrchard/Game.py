import random


class Game:

    def __init__(self):
        self.green_apples = 4
        self.red_apples = 4
        self.blue_plums = 4
        self.yellow_pears = 4
        self.crow_position = 6
        self._log = ''
        self._normalized_log_buffer = []
        self._normalized_log = ''


    def new_game(self):
        self.__init__()

    def is_game_won(self):
        if self.green_apples == 0 and self.red_apples == 0 and \
                self.blue_plums == 0 and self.yellow_pears == 0:
            return True
        else:
            return False

    def is_game_lost(self):
        return True if self.crow_position == 0 else False

    @staticmethod
    def roll_dice():
        return random.randint(0, 5)

    def move_green(self, is_strategic=False):
        if self.green_apples > 0:
            self.green_apples -= 1
        self.log('g', is_strategic)

    def move_red(self, is_strategic=False):
        if self.red_apples > 0:
            self.red_apples -= 1
        self.log('r', is_strategic)

    def move_blue(self, is_strategic=False):
        if self.blue_plums > 0:
            self.blue_plums -= 1
        self.log('b', is_strategic)

    def move_yellow(self, is_strategic=False):
        if self.yellow_pears > 0:
            self.yellow_pears -= 1
        self.log('y', is_strategic)

    def move_crow(self):
        self.crow_position -= 1
        # self.log('!')

    def move_strategically(self):
        choices = []
        if self.green_apples > 0:
            choices.append(self.move_green)
        if self.red_apples > 0:
            choices.append(self.move_red)
        if self.blue_plums > 0:
            choices.append(self.move_blue)
        if self.yellow_pears > 0:
            choices.append(self.move_yellow)

        random_index = random.randint(0, len(choices) - 1)
        f = choices[random_index]
        f(True)

    def log(self, s, is_strategic=False):
        if not is_strategic:
            self._log += s
        else:
            self._log += s.upper()

        if not is_strategic:
            self._normalized_log_buffer.append(s)
        else:
            self._normalized_log_buffer.sort()
            self._normalized_log += ''.join(self._normalized_log_buffer)
            self._normalized_log_buffer = []
            self._normalized_log += s.upper()

    def simulate_game(self, dice_sequence=None):
        self.new_game()

        turn_count = 0
        while True:

            if dice_sequence:
                roll = dice_sequence[turn_count]
            else:
                roll = self.roll_dice()

            if roll == 0:
                self.move_crow()
            elif roll == 1:
                self.move_green()
            elif roll == 2:
                self.move_red()
            elif roll == 3:
                self.move_blue()
            elif roll == 4:
                self.move_yellow()
            else:
                self.move_strategically()

            turn_count += 1

            if self.is_game_lost():
                self.log('L', True)
                win = False
                break

            if self.is_game_won():
                self.log('W', True)
                win = True
                break

        return win, turn_count, self._log, self._normalized_log
