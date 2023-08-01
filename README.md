ChaseTheAce Game Documentation
Welcome to the documentation for ChaseTheAce, a fun and interactive terminal-based card game. In ChaseTheAce, players are dealt a card from a standard 52-card deck and have the option to stick with their card or swap it with the deck or another player. The objective of the game is to avoid ending up with the lowest card, where Ace is the lowest and King is the highest.

Installation
Before running the game, make sure you have Python 3 installed on your system. To install the game, follow these steps:

Clone the ChaseTheAce repository from GitHub.
bash
Copy code
git clone https://github.com/bsjohnson20/ChaseTheAceMP
cd ChaseTheAce

Copy code
How to Play

Open your terminal and navigate to the ChaseTheAce directory.

Start the game by running the following command:

bash
Copy code
python chase_the_ace.py
The game will prompt you to enter the number of players who will be participating in the game. Each player will be dealt a card from the deck, and the game will begin.

The game will proceed in rounds, and each round consists of the following steps:

a. Players take turns to decide whether to stick with their card or swap it with the deck or another player. The player with the lowest card in the previous round goes first in the current round.

b. If it's the last player's turn or the dealer's turn, the player will not see their card until the end of the round.

c. If the previous player decides to swap and the current player chooses to swap as well, the two players will exchange cards. However, swapping with a player who has a King is not possible, and a player with a King cannot swap their card.

d. After all players have made their decisions, the dealer (last player) reveals their card to everyone and decides whether to swap it or not.

e. The round ends, and the players with the lowest card (Ace being the lowest and King the highest) will lose a life.

The game continues in rounds until one or more players run out of lives. The last remaining player(s) are declared winners.

Players can decide to exit the game at any time by entering "exit" when prompted for their decision.

Game Rules
Each player starts with 3 lives.

Ace is the lowest card, and King is the highest.

Swapping is not possible with a player who has a King, and a player with a King cannot swap their card.

The dealer, who goes last, will not see their card until the end of the round, and they can decide whether to swap it or not.

When a player loses all their lives, they are eliminated from the game.

Sample Gameplay
vbnet
Copy code
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

Player 1, it's your turn. Do you want to stick (S) or swap (W)? S

Player 2, it's your turn. Do you want to stick (S) or swap (W)? S

Player 3, it's your turn. Do you want to stick (S) or swap (W)? S

Player 4, it's your turn. Do you want to stick (S) or swap (W)? S

Player 1, it's your turn. Do you want to stick (S) or swap (W)? S

Player 2, it's your turn. Do you want to stick (S) or swap (W)? S

Player 3, it's your turn. Do you want to stick (S) or swap (W)? S

Player 4, it's your turn. Do you want to stick (S) or swap (W)? S

Dealer (Player 1), your card is: A. Do you want to stick (S) or swap (W)? W
Swapping your card with the deck...
Dealer (Player 1), your new card is: J

The round ends. Player 2, Player 3, and Player 4 lost a life.

... (Game continues until a player loses all lives)

Congratulations, Player 1! You won the game!

Thank you for playing ChaseTheAce. Hope you had fun!
Enjoy playing ChaseTheAce and have a great time with your friends!
