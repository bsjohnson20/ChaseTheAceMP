import logging
import random as rd


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
        pass # print("ValueError reached, moving on to match")

    match card:
        case "A":
            return 1
        case "J":
            return 11
        case "Q":
            return 12
        case "K":
            return 13


class Player:
    def __init__(self, lives, name="unknown"):
        self.lives = lives
        self.card = ""
        self.name = name


    def revealCard(self):
        print(f"Player: {self.name}\nYour card is: {self.card}.\n")

    def choose(self):
        print("\n#--------------------#\nIt is time to either swap your card or stick!")
        choice=""
        while choice == "":
            choice = input("Your choice (0 - stick, 1 - swap): ")
            return int(choice)


class ChaseTheAce:
    def __init__(self, lives=3, deflives=3, players_count=2):
        self.debugging = False
        self.deflives = deflives
        self.lives = lives
        self.players_count = players_count
        self.players = []
        self.cards = []
        print("Doing stuff!")
        self.setupPlayers()
        self.GameLoop()
        self.PlayerHistory=[]
    def GameLoop(self):
        while len(self.players)>1:
            input("Begin the new round! Press enter to begin:")
            self.setupcards() # reset cards
            self.handoutcards() # give each player a card
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

                    if len(self.players) == self.players.index(i)+1:
                        print("Swapping with deck card!")
                        card = rd.choice(self.cards)
                        self.cards.remove(card)
                        i.card = card
                        print(f"You obtained the card: {i.card}!")

                    elif self.players[index+1].card == "K":
                        print("DENIED! The next player has a king!")
                    else:
                        print("Swapping the cards now!")
                        self.players[index+1].card, self.players[index].card = self.players[index].card, self.players[index+1].card
                        print(f"Player {i.name} card is now: {i.card}\nPlayer {self.players[index+1].name} is now the {self.players[index+1].card}!")

            # assessing who's gonna die!
            print("\n\n#---------------------------------------#\n\n")
            print("Final stage - assessing who's dying")
            for i in self.players:
                # runs if it's the last dude
                if (len(self.players)==self.players.index(i)+1):
                    print(f"The lowest card is the {lowest_card}")
                    for i in range(len(self.players)):
                        if self.players[i].card == lowest_card:
                            self.players[i].lives -= 1
                            if self.players[i].lives == 0:
                                print(f"Sorry {self.players[i].name}, you have ran out of lives!")
                                self.PlayerHistory.append(self.players[i])
                                self.players[i].remove()
                            else:
                                print(f"{self.players[i].name} you had the card: {lowest_card} and thus you have lost a life! Remaining lives {self.players[i].lives}")
                                print("#-------------------------#\n\n")
                else:
                    if returnCardTier(i.card) < returnCardTier(self.players[self.players.index(i)+1].card):
                        lowest_card=i.card
                    else:
                        lowest_card=self.players[self.players.index(i)+1].card



                    print(f"Remaining players: {len(self.players)}")
                    for k in self.players:
                        print(k.name,end=', ')




        print("It seems we have a winner!")
        print(f"The winner is {self.players[0].name}")
        i = 0
        print("\nThe leaderboard:")
        for item in self.PlayerHistory:
            i+=1
            print(f"{i}: {item.name}")



    def setupPlayers(self):
        """
        sets up the players with a for loop, looping through till it's made every class object for every player
        :return:
        """
        logging.info("Starting setupPlayers")
        print("Setting up players!")
        # add players to the game
        for i in range(self.players_count):
            name = input("Input a name: ")
            newplayer = Player(lives=self.deflives, name=name)
            self.players.append(newplayer)
        logging.info("Finished SetupPlayers")

    def setupcards(self):
        for i in range(4):
            for item in (1,2,3,4,5,6,7,8,9,10,"J","Q","K"):
                self.cards.append(item)
        if self.debugging:
            print(self.cards)

    def handoutcards(self):
        for i in self.players:
            card = rd.choice(self.cards)
            self.cards.remove(card)

            i.card=card

            if self.debugging:
                print(card)
                print(self.cards)

        # randomly handout cards from a list

# start game
#Game = ChaseTheAce(lives=3,deflives=3)


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
DebugGame = ChaseTheAce(lives=3,deflives=3,players_count=2)
DebugGame.debugging = True
DebugGame.setupPlayers()
DebugGame.setupcards()
DebugGame.handoutcards()


