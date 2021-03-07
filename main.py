import random

from FirstOrchard.Game import Game
from FirstOrchard.PlayerPicksWorst import PlayerPicksWorst
from FirstOrchard.PlayerPicksBestWithBias import PlayerPicksBestWithBias


def gen_dice_sequence():
    length = 64
    ret = [0] * length
    for i in range(length):
        ret[i] = random.randint(0, 5)
    return ret


if __name__ == '__main__':
    total_simulations = 100000
    win_count = 0
    # game = Game(PlayerPicksWorst())
    game = Game(PlayerPicksBestWithBias())

    for _ in range(total_simulations):
        dice_rolls = gen_dice_sequence()
        win, moves, log, nlog = game.simulate_game(dice_sequence=dice_rolls)
        if win:
            win_count += 1

    win_percentage = (win_count / total_simulations) * 100
    print(win_percentage)

    # print(f'{total_simulations} sims | {win_count/total_simulations*100}% wins | {average_sum/total_simulations} moves')

'''
Results:
optimal_pick  10000 sims | 77.10000000000001% wins | 22.2137 moves
bias_pick     10000 sims | 76.78% wins | 22.3187 moves
random_pick   10000 sims | 73.97% wins | 23.1517 moves
worst_pick    10000 sims | 70.46% wins | 24.202 moves

https://colab.research.google.com/ for data analysis.

'''
