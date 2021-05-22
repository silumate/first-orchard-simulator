# tl;dr
Run simulations of the very simple "First Orchard" game for kids.

# Executing the program
```Python
python3 main.py
```

Look at the main method and uncomment the simulation you want to run.

# Background
I bought a simple board game to play with my two-year-old daughter: First Orchard (https://www.habausa.com/my-very-first-games-first-orchard/).

The game seemed easy enough to win, but I was curious how a good or bad strategy would affect the outcome.  I was concerned that my competitive side would drive me to criticize my two-year-old's choices.

Therefore I wrote this code to run simulations and predict how often we would win.  

It turns out the game is pretty easy to win, and the difference between making wise choices versus poor choices only adds about 10% to your odds of winning.
Hence, I stopped worrying about strategy. I watched my daughter learn how to set up the board, roll a die, put pieces away, and wait for her turn — elementary stuff.

The game is so easy to win; it's sometimes fun to root for the crow and lose the game.  

After playing for a couple of months, my daughter started using a strategy I had not expected: pick blue (her favourite colour).  I was a bit humbled by my inability to foresee that.  I updated my simulator and determined that this strategy alone wins about 2% more often than making the worst choice but making a random choice is 1% better.

# Example Output
Results from a run_simulations_with_all_strategies() with 100,000 simulations.

For a single player game:
| Win Rate | Strategy |
| -------- | -------- |
| 70.061%  | Make the worst possible move |
| 72.592%  | Pick your favourite color first |
| 73.742%  | Randomly pick a legal move |
| 76.845%  | Pick the color with the most left (and biased to a favorite if there is a tie) |
| 76.821%  | Pick the color with the most left (and randomly choose one if there is a tie) |
  
  ## Why 100,000 simulations?
  Because when I ran 10,000 simulations twice, the win rate seemed to vary by a couple of percentage points.  So I ran more simulations and the win rate varied less from one run of 100k simulations to the next.
