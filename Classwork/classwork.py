import random

class Deck():
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size
        
    
    def deal(self):
        # When the deck runs out cards (parameter passed into class)
        # We need to reshuffle the deck
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print("Reshuffling...!!!")
        # Adding 1 because there is no 0 in a deck of cards
        self.current_card += 1
        return self.card_list[self.current_card - 1]
    
def main():
    
    ranks = ['2', '3', '4', '5', '6', '7', '8','9', '10', 'J', 'Q', 'K', 'A']
    
    suits = ["clubs", "diamonds", "hearts", "spades"]
    
    my_deck = Deck(52)
    
    poker_hand_dict = {}
    
    #for i in range(12):
        #print(f'Deal #{i+1}')
    for i in range(5):
        d = my_deck.deal()
        r = d % 13
        s = d // 13
        print(ranks[r], "of", suits[s])
        poker_hand_dict[i] = (ranks[r], "of", suits[s])
    print()
    
    print(poker_hand_dict)
    replacement_list = []
    
    print("Please replace three cards. ")
    for i in range(3):
        poker_replace = int(input("Which card number (1-5) do you want to replace? "))
        # Subtract 1 to match replacement_list
        replacement_list.append(poker_replace - 1)
        print(replacement_list)
        
    for i in replacement_list:
        poker_hand_dict.pop(replacement_list[i])
    print(poker_hand_dict)
    
main()