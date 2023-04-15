
#imports the random library
import random


#giving the cards suits, ranks and values

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
          'Queen':10, 'King':10, 'Ace':11}


playing = True

#intiates a card with it's given suit and rank

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


#creates a deck of all given cards

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank)) 

    def __str__(self):
        deck_comp = '' 
        for card in self.deck:
            deck_comp += '\n '+card.__str__() 
        return 'The deck has:' + deck_comp

    def shuffle(self):          #shuffles the deck
        random.shuffle(self.deck)

    def deal(self):             #dealsa  card from the deck
        single_card = self.deck.pop()
        return single_card


#adds the starting cards to the players hand

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

#adds an extra card to the players hand

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

#ajusts the ace aloowing it to be either 1 or 10


    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

#creates a class for keeping track of the chips a player bets

class Chips:

    def __init__(self):
        self.total = 100  #can be set to a default value or as an input by the player
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


#function for taking bets
def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

#function for taking hits

def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()



#prompts player to hit or stand

def hit_or_stand(deck,hand):
    global playing  #controls a while loop

    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")

        if x[0].lower() == 'h':
            hit(deck,hand)  

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


#functions that display cards

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)


#handles end of game scenarios

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")






#game code

while True:
    #prints opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')

    #creates a deck, shuffles it then deals 2 cards to each player
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #set up the players chips
    player_chips = Chips()

    # Prompt the Player for their bet
    take_bet(player_chips)

    #shows cards but keeps one card on the dealer hidden
    show_some(player_hand,dealer_hand)

    while playing:

        #prompt for player to hit or stand
        hit_or_stand(deck,player_hand)

        #shows cards but keeps one card on the dealer hidden
        show_some(player_hand,dealer_hand)

        #if players hand is over 21 it will run player_busts() and break the loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break


            #if the player hasnt busted keep playing until the dealers hand reaches 17
    if player_hand.value <= 21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

            #shows all cards
        show_all(player_hand,dealer_hand)

        #runs different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)

            #tells a player their total chips
    print("\nPlayer's winnings stand at",player_chips.total)

    #asks to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break


#end of program