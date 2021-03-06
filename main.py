import random
import csv

from FirstOrchard.Game import Game
from FirstOrchard.GameOptimalWithoutBias import GameOptimalWithoutBias
from FirstOrchard.GameOptimalWithBias import GameOptimalBiased
from FirstOrchard.GameWorstPick import GameWorstPick


def gen_dice_sequence():
    length = 64
    ret = [0] * length
    for i in range(length):
        ret[i] = random.randint(0, 5)
    return ret


if __name__ == '__main__':
    sims = [
        GameWorstPick(),
        Game(),
        GameOptimalBiased(),
        GameOptimalWithoutBias()
    ]
    sim_cnt = len(sims)

    win_count = [0] * len(sims)
    total_simulations = 100000

    with open('sims.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for _ in range(total_simulations):
            dice_rolls = gen_dice_sequence()

            row = [None] * 2 * sim_cnt
            col = 0

            for i, sim in enumerate(sims):
                win, moves, log, nlog = sim.simulate_game(dice_sequence=dice_rolls)
                row[col] = win
                col += 1
                row[col] = nlog
                col += 1
                if win:
                    win_count[i] += 1

            csvwriter.writerow(row)

    win_percentage = [(x / total_simulations) for x in win_count]
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
