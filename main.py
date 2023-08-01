import csv
import logging
import os
import random as rd
import sys


# The game works by having the lowest number in a deck meaning you lose!
# 3 lives
# Higher the number the less likely to die
# Can't swap if a guy has a king

def returnCardTier(card):
    try:
        return int(card)

    except TypeError:
        print("TypeError reached, this should not occur!")
        return 0
    except ValueError:
        pass  # print("ValueError reached, moving on to match")

    match card:
        case "A":
            return 1
        case "J":
            return 11
        case "Q":
            return 12
        case "K":
            return 13


class ChaseTheAce:

    def __init__(self, lives=3, deflives=3, players_count=2, selfplaying=False, debugging=False):
        self.debugging = debugging
        self.deflives = deflives
        self.lives = lives
        self.players_count = players_count
        self.players = []
        self.cards = []
        self.selfplaying = selfplaying
        self.PlayerHistory = set()
        print("Doing stuff!")

        # begin
        self.setup()

    def setup(self):
        self.setupPlayers()
        self.GameLoop()

    def GameLoop(self):
        while len(self.players) > 1:
            if not self.selfplaying:
                input("Begin the new round! Press enter to begin:")
            self.setupcards()  # reset cards
            self.handoutcards()  # give each player a card
            print("\n\n#----------------------#\n\nRevealing Cards to players now:\n")
            for i in self.players:
                i.revealCard()
            for i in self.players:
                print(f"#------------------------#\nIt is player {i.name}'s turn!\n#------------------#\n\n")
                choice = i.choose()
                if choice == 0:
                    print(f"The player called {i.name} has chosen to Stick!\n")
                elif choice == 1:
                    print(f"The player called {i.name} has chosen to Swap!\n")
                    index = self.players.index(i)

                    # If last player in list then swap with deck card
                    if len(self.players) == self.players.index(i) + 1:
                        print("Swapping with deck card!")
                        card = rd.choice(self.cards)
                        self.cards.remove(card)
                        i.card = card
                        print(f"You obtained the card: {i.card}!")
                    # Denied if next player has a king
                    elif self.players[index + 1].card == "K":
                        print("DENIED! The next player has a king!")
                    else:
                        # otherwise swap with next player
                        print("Swapping the cards now!")
                        self.players[index + 1].card, self.players[index].card = self.players[index].card, self.players[
                            index + 1].card
                        print(
                            f"Player {i.name} card is now: {i.card}\nPlayer {self.players[index + 1].name} is now the {self.players[index + 1].card}!")

            # assessing who's gonna die!
            print("\n\n#---------------------------------------#\n\n")
            print("Final stage - assessing who's dying")
            for i in self.players:
                # runs if it's the last dude
                if (len(self.players) == self.players.index(i) + 1):
                    print(f"The lowest card is the {lowest_card}")
                    for i in self.players:
                        if self.players[self.players.index(i)].card == lowest_card:
                            self.players[self.players.index(i)].lives -= 1
                            if self.players[self.players.index(i)].lives == 0:
                                print(f"Sorry {i.name}, you have ran out of lives!")
                                self.PlayerHistory.add(i)
                                self.players.remove(i)
                            else:
                                print(
                                    f"{i.name} you had the card: {lowest_card} and thus you have lost a life! Remaining lives {i.lives}")
                                print("#-------------------------#\n\n")
                else:
                    if returnCardTier(i.card) < returnCardTier(self.players[self.players.index(i) + 1].card):
                        lowest_card = i.card
                    else:
                        lowest_card = self.players[self.players.index(i) + 1].card

                    print(f"Remaining players: {len(self.players)}")
                    for k in self.players:
                        print(k.name, end=', ')

        print("It seems we have a winner!")
        print(f"The winner is {self.players[0].name}")
        i = 0
        print("\nThe leaderboard:")
        for item in self.PlayerHistory:
            i += 1
            print(f"{i}: {item.name}")

        # write to csv
        self.update_scores()

        # play again
        if not self.selfplaying:
            again = input("Would you like to play again? (y/n): ")
            if again == "y":
                self.setup()

    def setupPlayers(self):
        """
        sets up the players with a for loop, looping through till it's made every class object for every player
        :return:
        """
        logging.info("Starting setupPlayers")
        print("Setting up players!")
        # clear players
        self.players = []
        # add players to the game
        if not self.selfplaying:
            for i in range(self.players_count):
                name = input("Input a name: ")
                newplayer = Player(lives=self.deflives, name=name, selfplaying=self.selfplaying)
                self.players.append(newplayer)
        else:
            for i in range(self.players_count + 1):
                name = f"Robot {i}"
                newplayer = Player(lives=self.deflives, name=name, selfplaying=self.selfplaying)
                self.players.append(newplayer)
        logging.info("Finished SetupPlayers")

    def setupcards(self):
        self.cards = []  # clear cards
        for i in range(4):
            for item in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"):
                self.cards.append(item)
        if self.debugging:
            print(self.cards)

    def handoutcards(self):

        for i in self.players:
            card = rd.choice(self.cards)
            self.cards.remove(card)

            i.card = card

            if self.debugging:
                print(card)
                print(self.cards)

    def update_scores(self):
        try:
            with open("scores.csv", "r") as f:
                reader = csv.reader(f, delimiter=",")
                scores = list(reader)

            # check if player is in scores
            score = 4
            for i in self.PlayerHistory:
                if not (score == 0):
                    score -= 1
                for k in scores:
                    if k[0] == i.name:
                        k[1] = int(k[1]) + score
                        break
                else:
                    scores.append([i.name, score])

            # sort scores skip first row by deleting it
            del scores[0]
            scores.sort(key=lambda x: int(x[1]), reverse=True)
            scores.insert(0, ["Name", "Score"])

            # write to csv
            with open("scores.csv", "w") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerows(scores)

        except FileNotFoundError:
            scores = [["Name", "Score"]]
            print("File not found, creating new file")
            with open("scores.csv", "w") as f:
                writer = csv.writer(f, delimiter=",")
                writer.writerows(scores)

        except IndexError:
            print("No players have won yet!")
            # delete file
            os.remove("scores.csv")
            # loop
            self.update_scores()


class Player:
    def __init__(self, lives, name="unknown", selfplaying=False):
        self.lives = lives
        self.card = ""
        self.name = name
        self.selfplaying = selfplaying

    def revealCard(self):
        print(f"Player: {self.name}\nYour card is: {self.card}.\n")

    def choose(self):
        print("\n#--------------------#\nIt is time to either swap your card or stick!")
        choice = ""
        if self.selfplaying:
            choice = rd.randint(0, 1)
            print(f"Robot Player {self.name} has chosen {choice}")
            return choice
        while choice == "":
            choice = input("Your choice (0 - stick, 1 - swap): ")
            return int(choice)


# start game
Game = ChaseTheAce(lives=3, deflives=3)


# Game.setupPlayers()
# Game.GameLoop()


# test suite
# test 1 - setup players
# test 2 - setup cards
# test 3 - handout cards
# test 4 - reveal cards
# test 5 - choose
# test 6 - swap
# test 7 - stick
# test 8 - assess who's dying
# test 9 - remove player
# test 10 - end game
# test 11 - leaderboard

# test 1 - setup players
def test():
    for i in range(500):
        print(f"Test 1 - setup players - {i + 1}")
        Game = ChaseTheAce(lives=3, deflives=3, players_count=10, selfplaying=True, debugging=True)
    # DebugGame = ChaseTheAce(lives=3,deflives=3,players_count=2,selfplaying=True,debugging=True)


if __name__ == "__main__":
    # check sys args for --test
    if "--test" in sys.argv:
        test()
    else:
        # check for player count with --players
        if "--players" in sys.argv:
            try:
                playercount = int(sys.argv[sys.argv.index("--players") + 1])
            except ValueError:
                playercount = 4
        else:
            playercount = 4
        Game = Game = ChaseTheAce(lives=3, deflives=3, players_count=playercount)
