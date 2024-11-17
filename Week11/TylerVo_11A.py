#Tyler Vo
#11/17/2024

import random

class Deck:
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        # Reshuffle the deck when it runs out of cards
        if self.current_card >= self.size:
            random.shuffle(self.card_list)
            self.current_card = 0
            print("Reshuffling...!!!")
        # Deal the next card
        card = self.card_list[self.current_card]
        self.current_card += 1
        return card

def main():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ["clubs", "diamonds", "hearts", "spades"]
    my_deck = Deck(52)

    poker_hand_dict = {}
    
    # Deal initial poker hand (5 cards)
    print("Initial poker hand:")
    for i in range(5):
        d = my_deck.deal()
        r = d % 13
        s = d // 13
        poker_hand_dict[i] = (ranks[r], suits[s])
        print(f"Card {i+1}: {ranks[r]} of {suits[s]}")
    print()

    # Replace cards
    print("You can replace up to 3 cards.")
    replacement_list = []
    for _ in range(3):
        try:
            poker_replace = int(input("Which card number (1-5) do you want to replace? (Enter 0 to skip): "))
            if poker_replace == 0:
                break
            if 1 <= poker_replace <= 5 and poker_replace - 1 not in replacement_list:
                replacement_list.append(poker_replace - 1)
            else:
                print("Invalid input. Try again.")
        except ValueError:
            print("Please enter a valid number.")
    print()

    # Ensure replaced cards are not re-dealt
    removed_cards = [poker_hand_dict[i] for i in replacement_list]

    # Replace selected cards with new ones
    for i in replacement_list:
        while True:
            d = my_deck.deal()
            r = d % 13
            s = d // 13
            new_card = (ranks[r], suits[s])
            if new_card not in removed_cards:  # Ensure the new card is not in removed cards
                poker_hand_dict[i] = new_card
                break

    # Print final poker hand
    print("\nFinal poker hand:")
    for i in range(5):
        card = poker_hand_dict[i]
        print(f"Card {i+1}: {card[0]} of {card[1]}")
    print()

main()
