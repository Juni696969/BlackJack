import random
import Stackss
# in black jack the face cards (J,Q,K) are 10 and the Ace is either 1 or 11
# In order to win the player should have a closer number to 21 than the dealer
# The dealer stops pulling cards at 17 
# If the player or the dealer pass 21 they loose. 

#start of by creating the deck of cards


deck = [2,3,4,5,6,7,8,9,
        2,3,4,5,6,7,8,9,
        2,3,4,5,6,7,8,9,
        2,3,4,5,6,7,8,9,
        "J", "Q","K", "A"
        "J", "Q","K", "A"
        "J", "Q","K", "A"
        "J", "Q","K", "A"]*6

# There are four cards of the same type because there are 4 different colors.
# we multiply the string by 6 because there are 6 decks in a game of BJ
# Now we create a players hand as an empty array aswell.

p_handQueue= ()

# Same step for dealers hand

d_handQueue = ()

# Player and dealer situation 
playersit = True # boolean to see if player is in the game or lost 
Dealersit = True # boolean to see if dealer is in the game or lost 

# A function to deal crads

def dealing(given):
    card = random.choice(deck)
    if len(deck)>0:
        return None
    given.enqueue(card) # using enqueue to add a card to player hand
    deck.dequeue(card) # using dequeue to remove a card from the deck 

# Let us calculate the value of each hand

def value(given):
        face_cards = ["J", "Q", "K"] # these cards are worth 10 
        total = 0 # initiate a counter and append to it later on 
        for card in given:  #looping the function 
                if card in range (1,11): # checking if the card has a vlue of 1 to 10
                        total += card # then we add the value of thacard to the total 
                elif card in face_cards: # if the card is a face card 
                        total += 10 # add 10 to the total 
                else:
                        if total >=  11:  # this function is for the ace card, the ace can be one or 11
                                # if the total is larger or equal to 11  and an Ace card is pulled out of the deck then the value is 1
                                total += 1 # add 1 to the total 
                        elif total <= 10: # if the total is smaller or equal to 10 
                                total += 11 # add 11 to the total 
        return total 

# See the winner 

def ViewDealerdeck(): 
        if len(d_handQueue) == 2: 
                return d_handQueue.first
        

# Code the Game 
for _ in range(2):
        dealing(p_handQueue) # using recursion, recalling a function 
        dealing(d_handQueue) # using recursion, recalling a function 

while playersit or Dealersit: 
        print("The dealer has", ViewDealerdeck())
        print("You have", p_handQueue, "  =  ", value(p_handQueue))
        if playersit:
                choice = input("1: Stand \n 2: Hit")
        if value(d_handQueue)>16:# if dealer has more than 16 he stands
                Dealersit = False #dealer stands 
        else:
                dealing(d_handQueue) # if dealer has less than 16 he draws another card
        if choice == "1": # if user chooses to stand
                playersit = False # no cards have been drawn 
        else: 
                dealing(p_handQueue) # if player chooses to hit, puls a card 
        if value(p_handQueue)>=21: # if the player has more than 21 he loses
                break # stop the loop 
        elif value(d_handQueue) >= 21: # if dealer has more than 21 he loses 
                break # stop the loop 


        # Putting the rules of the game and how the game is won
        if value(p_handQueue) == 21:
                print("\nYou have", p_handQueue, "BLACKJACK")
                print("The dealer has", value(d_handQueue))
        elif value(d_handQueue) == 21:
                print("\n The dealer has", d_handQueue, "BJ")
                print("Dealer wins :(")
        elif value(p_handQueue)==value(d_handQueue)==21:
                print("You both have blackjack, it is a tie")
                print("\n Player hand:", p_handQueue)
                print("\n Dealer hand: ", d_handQueue)
        elif value(p_handQueue)>21:
                print("Busted. You loose")
                print("\n Player hand:", p_handQueue)
                print("\n Dealer hand: ", d_handQueue)
        elif value(d_handQueue)>21:
                print("Dealer has busted")
                print("\n Player hand:", p_handQueue)
                print("\n Dealer hand: ", d_handQueue)
        elif 21 - value(d_handQueue) < 21 - value(p_handQueue):
                print("The dealer wins")
                print("\n Player hand:", p_handQueue)
                print("\n Dealer hand: ", d_handQueue)
        elif 21 - value(p_handQueue) < 21 - value(d_handQueue):
                print("You win")
                print("\n Player hand:", p_handQueue)
                print("\n Dealer hand: ", d_handQueue)
        elif value(p_handQueue) == value(d_handQueue):
                print("Push-- It is a tie")
                print("\n Player hand:", p_handQueue)
                print("\n Dealer hand: ", d_handQueue)