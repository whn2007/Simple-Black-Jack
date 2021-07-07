import random

def get_player_total(player_value):
    player_total = 0
    for card in range(len(player_value)):
        if player_value[card] != 'A':
            player_total += player_value[card]
        else:
            temp = player_value.pop(card)
            player_value.insert(0,temp)
    
    for card in range(len(player_value)):
        valid = ['1','11']
        print('Current total without Ace cards is {}.'.format(player_total))
        if player_value[card] == 'A' and player_total <= 21:
            a_value = (input('\nWould you like your Ace to be valued at (1) or (11)?'))
            while a_value not in valid:
                print("Please enter a correct value.\n")
                a_value = (input('\nWould you like your Ace to be valued at (1) or (11)?'))
            player_total += int(a_value)
    return player_total

def get_dealer_total(dealer_value):
    dealer_total = 0
    for card in range(len(dealer_value)):
        if dealer_value[card] != 'A':
            dealer_total += dealer_value[card]
        else:
            temp = dealer_value.pop(card)
            dealer_value.insert(0,temp)
    
    for card in range(len(dealer_value)):
        if dealer_value[card] == 'A':
            if dealer_total < 17 and dealer_total + 11 <= 17:
                dealer_total += 11
            else:
                dealer_total += 1
    return dealer_total



def blackjack():
    print('Hello welcome to Blackjack!\n')
    deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'A','A','A','A']
    player_hold = False
    player_value = []
    dealer_value = []
    dealer_shown_card = 0
    player_total = 0
    dealer_total = 0

    value_one = random.randrange(len(deck))
    player_card_one = deck[value_one]
    print('Dealer deals player a {}.'.format(player_card_one))
    deck.pop(value_one)
    player_value.append(player_card_one)

    value_two = random.randrange(len(deck))
    dealer_card_one = deck[value_two]
    print('Dealer deals himself a {}.'.format(dealer_card_one))
    dealer_shown_card = dealer_card_one
    deck.pop(value_two)
    dealer_value.append(dealer_card_one)

    value_three = random.randrange(len(deck))
    player_card_two = deck[value_three]
    print('Dealer deals player a {}.'.format(player_card_two))
    deck.pop(value_three)
    player_value.append(player_card_two)

    value_four = random.randrange(len(deck))
    dealer_card_two = deck[value_four]
    print('Dealer deals himself a (hidden) card.')
    deck.pop(value_four)
    dealer_value.append(dealer_card_two)

    
    player_total = get_player_total(player_value)

    dealer_total = get_dealer_total(dealer_value)
    print('Dealer total is hidden.')
    print('Player total is {}.\n'.format(player_total))

    while player_total < 21 and player_hold != True:
        player_choice = input("Would you like to (I)nspect dealer's card, (H)it, or H(O)ld?")
        while player_choice not in "IiHhOo":
            player_choice = input("Would you like to (I)nspect dealer's card, (H)it, or H(O)ld?")
        if player_choice in 'Ii':
            print("Dealer's revealed card is {}.\n".format(dealer_shown_card))
        elif player_choice in "Oo":
            player_hold = True
        elif player_choice in "Hh":
            new_card = random.randrange(len(deck))
            player_new_card = deck[new_card]
            print('Dealer deals player a {}.'.format(player_new_card))
            deck.pop(new_card)
            player_value.append(player_new_card)
            player_total = get_player_total(player_value)
            print('Player total is {}.\n'.format(player_total))
    
    while dealer_total < 17:
        temp_val = random.randrange(len(deck))
        new_dealer_card = deck[temp_val]
        deck.pop(temp_val)
        dealer_value.append(new_dealer_card)
        dealer_total = get_dealer_total(dealer_value)
            
    if player_total > 21:
        print('\nYour total is {}. You lose!\n'.format(player_total))
    elif dealer_total > 21:
        print('\nDealer total is {}. Dealer has busted. You win!\n'.format(dealer_total))
    elif player_total == 21 and dealer_total == 21:
        print('\nBoth player and dealer have a total of 21. Draw!\n')
    elif player_total == 21 and dealer_total != 21:
        print('Blackjack! You win!')
    elif player_total != 21 and dealer_total == 21:
        print('\nBlackjack! Dealer has a total of 21. Dealer wins!\n')
    elif player_total > dealer_total:
        print("\nPlayer's total is {}. Dealer's total is {}. Player wins!\n".format(player_total,dealer_total))
    elif dealer_total > player_total:
        print("\nPlayer's total is {}. Dealer's total is {}. Dealer wins!\n".format(player_total,dealer_total))
    else:
        print("\nPlayer and Dealer both have a total of {}. Match is a draw!\n".format(player_total))

play_again = True
while play_again == True:
    blackjack()
    player_answer = input('Would you like to play again? (Y)es / (N)o')
    while player_answer not in "YNyn" :
        player_answer = input('Would you like to play again? (Y)es / (N)o')
    if player_answer in 'Nn':
        play_again = False

print('Thank you for playing!')