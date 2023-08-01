# ChaseTheAce - Terminal-Based Card Game

ChaseTheAce is a fun and interactive terminal-based card game where players are dealt a card from a standard 52-card deck. The objective of the game is to avoid ending up with the lowest card, where Ace is the lowest, and King is the highest. Each player starts with 3 lives, and the player(s) with the lowest card after each round lose a life.

## How to Run the Game

To play ChaseTheAce, follow these steps:

1. Clone the ChaseTheAce repository from GitHub:

```
git clone https://github.com/your_username/ChaseTheAce.git
cd ChaseTheAce
```

2. Install the required Python dependencies: - there aren't any

```
pip install -r requirements.txt
```

3. Run the game using the following command:

```
python chase_the_ace.py
```

4. The game will prompt you to enter the number of players participating in the game.

## How to Play

1. At the start of the game, each player is given a singular card from the deck.

2. Players take turns in order to decide whether to stick with their card or swap it with the deck or another player. The player with the lowest card in the previous round goes first in the current round.

3. If it's the last player's turn or the dealer's turn, the player will not see their card until the end of the round.

4. Swapping is not possible with a player who has a King, and a player with a King cannot swap their card.

5. After all players have made their decisions, the dealer (last player) reveals their card to everyone and decides whether to swap it or not.

6. The round ends, and the players with the lowest card (Ace being the lowest and King the highest) will lose a life.

7. The game continues in rounds until one or more players run out of lives. The last remaining player(s) are declared winners.

## Leaderboards

The game keeps track of player scores and maintains a leaderboard. The scores are updated at the end of each game, and the leaderboard ranks players based on their scores (the number of rounds survived). The leaderboard data is stored in a CSV file named "scores.csv."

## Test Facility

You can enable the test facility to run automated test cases for the game. To do this, use the `--test` command-line argument when running the game:

```
python chase_the_ace.py --test
```

The test facility will execute a series of test cases to check different aspects of the game's functionality, such as setup, card distribution, player choices, leaderboard updates, and more.

## Example Gameplay

Here's an example of how the game works:

```
Welcome to ChaseTheAce!

Enter the number of players: 4
Player 1, your card is: 7
Player 2, your card is: K
Player 3, your card is: 2
Player 4, your card is: Q

Player 3, it's your turn. Do you want to stick (S) or swap (W)? W
Choose a player to swap with (1-4): 4
Swapping cards with Player 4...
Player 3, your new card is: Q

Player 4, it's your turn. Do you want to stick (S) or swap (W)? S

Player 1, it's your turn. Do you want to stick (S) or swap (W)? S

Player 2, it's your turn. Do you want to stick (S) or swap (W)? S

Player 3, it's your turn. Do you want to stick (S) or swap (W)? S

Player 4, it's your turn. Do you want to stick (S) or swap (W)? S

Dealer (Player 1), your card is: A. Do you want to stick (S) or swap (W)? W
Swapping your card with the deck...
Dealer (Player 1), your new card is: J

The round ends. Player 2, Player 3, and Player 4 lost a life.

Congratulations, Player 1! You won the game!

Thank you for playing ChaseTheAce. Hope you had fun!
```

Enjoy playing ChaseTheAce with your friends and see who can survive the longest in this exciting card game!
