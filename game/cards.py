#!/usr/bin/python3
import math
import random
import player

class card:
    def __init__(self, name, classification):
        self.name = name
        self.classification = classification
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = self.name + name
    def getClassification(self):
        return self.classification
    def setClassification(self, classification):
        self.classification = self.classification
#Function to create and set dictionary to hold cards
def setDeck():
    deck = {}
    for i in range (0, 52):
        #Set card values
        value = i % 13;
        if (value > 0 and value < 10):
            deck[i] = card(str(value+1), value+1)
        if (value == 0):
            deck[i] = card("Ace", 14)
        if (value == 10):
            deck[i] = card("Jack", 11)
        if (value == 11):
            deck[i] = card("Queen", 12)
        if (value == 12):
            deck[i] = card("King", 13)
        #Set card suits
        if (i > -1 and i < 13):
            deck[i].setName(" of Spades")
        if (i > 12 and i < 26):
            deck[i].setName(" of Hearts")
        if (i > 25 and i < 39):
            deck[i].setName(" of Clubs")
        if (i > 38 and i < 52):
            deck[i].setName(" of Diamonds")
    return deck

#Function to create and set cards_dealt vector
def setCardsDealt():
    cards_dealt = {}
    for i in range (0, 52):
        cards_dealt[i] = 0
    return cards_dealt

#Function to draw a random card
def draw(deck, cards_dealt):
    deck_index = random.randint(0,51)
    #check if random index is the same as one that's already in use
    if (cards_dealt[deck_index] == 0):
        cards_dealt[deck_index] = 1
        return deck[deck_index]
    return draw(deck, cards_dealt)

#Function to set the flop
def dealFlop(deck, cards_dealt):
    pool = {}
    burn = {}
    burn[0] = draw(deck, cards_dealt)
    pool[0] = draw(deck, cards_dealt)
    pool[1] = draw(deck, cards_dealt)
    pool[2] = draw(deck, cards_dealt)
    return pool

#Function to deal the turn card
def dealTurn(deck, cards_dealt, pool, burn):
    burn[1] = draw(deck, cards_dealt)
    pool[3] = draw(deck, cards_dealt)
    return pool

#Function to deal the river card
def dealRiver(deck, cards_deal, pool, burn):
    burn[2] = draw(deck, cards_dealt)
    pool[4] = draw(deck, cards_dealt)
    return pool


#DONE
def sortHand(hand_vec):
    #Quicksort later if this is causing a time issue
    for i in range(0,7):
        for j in range(0,7):
            if (hand_vec[j].classification > hand_vec[i].classification):
                temp = hand_vec[i]
                hand_vec[i] = hand_vec[j]
                hand_vec[j] = temp
    return hand_vec

#UNFINISHED
def straightFlush(hand_vec):
    #given flush
    #if normal flush return 0
    #if straight flush return 1
    #if royal flush return 2
    return 0

#UNFINISHED
#Function to return a hand ranking 1-10
#May have to edit later to include high card to differentiate same ranking
def classifyHand(hand_vec):
    #First we should sort the hand based on values(bubble-sort of 7 elements is negligible)
    hand_vec = sortHand(hand_vec)

    #CHECK FOR FLUSH(everything that stems out of flush)
    k = 0
    hand_vec_length = len(hand_vec)
    flush_count = {}
    flush_count["spades"] = 0
    flush_count["hearts"] = 0
    flush_count["clubs"] = 0
    flush_count["diamonds"] = 0
    flush = False

    #Loop once through hand to count the number of each suit
    while (k < hand_vec_length):
        if (hand_vec[k][-6:] == "Spades"):
            flush_count["spades"] = flush_count["spades"] + 1
            if (flush_count["spades"] > 4):
                flush  = True
        if (hand_vec[k][-6:] == "Hearts"):
            flush_count["hearts"] = flush_count["hearts"] + 1
            if (flush_count["hearts"] > 4):
                flush  = True
        if (hand_vec[k][-5:] == "Clubs"):
            flush_count["clubs"] = flush_count["clubs"] + 1
            if (flush_count["clubs"] > 4):
                flush  = True
        if (hand_vec[k][-8:] == "Diamonds"):
            flush_count["diamonds"] = flush_count["diamonds"] + 1
            if (flush_count["diamonds"] > 4):
                flush  = True
    #Must calculate the highest flush either here or in handRanking
    if (flush):
        return 6
        #flush_type = straightflush(hand_vec)

    #CHECK FOR STRAIGHT(double loop)
    #Need to edit for Ace(change classifier, add a condition, ect)?
    straight1 = False
    straight2 = False
    straight3 = False
    for i in range(0, 3):
        straight1 = True
        straight2 = True
        straight3 = True
        for j in range(i+1, i+5):
            if (test_vec[i].getClassification() + j != test_vec[j].getClassification()):
                if (i == 0): straight1 = False
                if (i == 1): straight2 = False
                if (i == 2): straight3 = False

    #Consider test case:
    if (straight3 == True):
        print(5.3)
    if (straight2 == True):
        print(5.2)
    if (straight1 == True):
        print(5.1)

    #CHECK FOR PAIR(everything that stems out of pair)
    #first_pair will only hold a pair
    first_pair = {}
    #second_pair will hold 2nd pair, triplets, or 4 of kind if applicable
    second_pair = {}
    for i in range()

#UNFINISHED
#Function to rank who has the best hand at the end of a round
#Make scalable later, for now 4 players
def handRanking(player_vector, pool):
    player_vector_index = 0
    hand_rankings = {}
    while (player_vector_index < player_vector.size()):
        #If the player has reached the end of the final betting phase
        if (player_vector[player_vector_index].getStatus() == 1):
            hand_vec = player_vector[player_vector_index].getHand()
            hand_vec[2] = pool[0]
            hand_vec[3] = pool[1]
            hand_vec[4] = pool[2]
            hand_vec[5] = pool[3]
            hand_vec[6] = pool[4]
            handRankings[player_vector_index] = classifyHand(hand_vec)


        player_vector_index = player_vector_index + 1
    return "winning hand is"