import random 



def create_deck():
    deck=[]
    for i in range(2, 11):
        for j in range ('♥','♠','♦','♣'):
            deck.append(str(i)+j)
    
    for i in ('j','Q','k','T'):
        for j in ('♥','♠','♦','♣'):
            deck.append(i+j)
    return deck



def started_hand(deck):
    hand = []
    for i in range():
        hand.append(random.choice(deck))
        deck.remove(hand[-])
    return hand, deck


def start_game():
    deck= create_deck()
    hand= []
    hand,deck= started_hand(deck)
    

        


start_game()