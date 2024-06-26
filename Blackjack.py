import random
from replit import clear 
import time 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def del_cart():
    
    return random.choice(cards)

def game():
    print("Welcome to Blackjack")
    print("Let's play")
    anser=input("Do you want paly Blackjack 'y' or 'n'")
    clear()
    if anser == 'y':
        print("YYY let's Blackjack begins")
        user_cards = [] 
        computer_cards = []
        while True:
            if anser == 'y':
                user_cards.append(del_cart())
            if sum(computer_cards)<17:
                computer_cards.append(del_cart())
            print(f"Your cartes are : {user_cards} | your sommes are : {sum(user_cards)}")
            print(f"The computer card is {computer_cards[0]}")
            if sum(user_cards) == 21:
                print("You win")
                break
            elif sum(computer_cards) == 21:
                print("Computer win")
                break
            if anser=='n':
                if sum(user_cards) == sum(computer_cards):
                    print("Draw")
                    break
                elif sum(user_cards) < sum(computer_cards)<21 or sum(user_cards)>sum(computer_cards)>21 :
                    print("computer win")
                    break
                elif sum(computer_cards) < sum(user_cards)<21 or sum(computer_cards)>sum(user_cards)>21 :
                    print("You win")
                elif sum(user_cards) > 21:
                    print("You lose")
                    break
                elif sum(computer_cards) > 21:
                    print("You win")
                    break
                break
            anser=input("You want to add another card 'y' or 'n'")
        print(f"The score is:\n\t\t user :{sum(user_cards)} | computer :{sum(computer_cards)}")
        time.sleep(10)
        clear()
        game()
game()



