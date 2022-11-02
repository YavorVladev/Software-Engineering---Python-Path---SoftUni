deck_of_cards = input().split(" ")
count_shuffle = int(input())
for shuffle in range(count_shuffle):
    end_deck = []  # Resets the deck after every shuffle. If it's last shuffle
    # it doesn't reset and "deck_of_cards" gets its value
    # therefore the "for loop" breaks and prints out "deck_of_cards"
    middle_deck = len(deck_of_cards) // 2
    left_side = deck_of_cards[:middle_deck]
    right_side = deck_of_cards[middle_deck:]
    for index in range(len(left_side)):
        end_deck.append(left_side[index])
        end_deck.append(right_side[index])
    deck_of_cards = end_deck
print(deck_of_cards)
