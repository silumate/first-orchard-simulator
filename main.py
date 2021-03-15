import random
import csv

from FirstOrchard.Game import Game
from FirstOrchard.Player import Player
from FirstOrchard.PlayerPicksWorst import PlayerPicksWorst
from FirstOrchard.PlayerPicksBestWithBias import PlayerPicksBestWithBias
from FirstOrchard.PlayerPicksBestWithoutBias import PlayerPicksBestWithoutBias
from FirstOrchard.PlayerPicksFavourite import PlayerPicksFavorite


def gen_dice_sequence():
    length = 64
    ret = [0] * length
    for i in range(length):
        ret[i] = random.randint(0, 5)
    return ret


def run_simulations_with_one_strategy():
    total_simulations = 100000
    win_count = 0
    # game = Game([PlayerPicksWorst()])
    game = Game([PlayerPicksFavorite()])

    for _ in range(total_simulations):
        dice_rolls = gen_dice_sequence()
        win, moves, log, nlog = game.simulate_game(dice_sequence=dice_rolls)
        if win:
            win_count += 1

    win_percentage = (win_count / total_simulations) * 100
    print(win_percentage)


def run_simulations_with_all_strategies():
    """
    Generate a sequence of dice rolls and use it to simulate single player games with each player strategy.
    Repeat thousands of times to compare how each strategy fares relative to each other.
    Results are saved in a CSV file for analysis.
    :return:
        None
    """
    sims = [
        Game([PlayerPicksWorst()]),
        Game([PlayerPicksFavorite()]),
        Game([Player()]),
        Game([PlayerPicksBestWithBias()]),
        Game([PlayerPicksBestWithoutBias()]),
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


def run_simulation_of_my_family():
    """
    My daughter plays like PlayerPicksFavorite(), my wife and I play like PlayerPicksBestWithoutBias().
    Simulations show that we will win about 75% of the time.

    :return: None
    """
    total_simulations = 100000
    win_count = 0
    game = Game([PlayerPicksFavorite(), PlayerPicksBestWithoutBias(), PlayerPicksBestWithoutBias()])

    for _ in range(total_simulations):
        dice_rolls = gen_dice_sequence()
        win, moves, log, nlog = game.simulate_game(dice_sequence=dice_rolls)
        if win:
            win_count += 1

    win_percentage = (win_count / total_simulations) * 100
    print(win_percentage)



if __name__ == '__main__':
    # run_simulations_with_one_strategy()
    # run_simulations_with_all_strategies()
    run_simulation_of_my_family()
'''
Example Result from a run_simulations_with_all_strategies() with 100,000 simulations
%           Player Strategy
0.70061     Make the worst possible move
0.72592     Pick your favourite color first
0.73742     Randomly pick a legal move
0.76845     Pick the color with the most left (and biased to your favorite if there is a tie)
0.76821     pick the color with the most left (and randomly choose one if there is a tie)
'''
