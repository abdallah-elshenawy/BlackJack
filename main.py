import random
import time
import os

def clear_screen():
   os.system("cls" if os.name == "nt" else "clear")

def deal_cards():
   """
   Returns a random card
   """

   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   return random.choice(cards)

def calculate_score(cards):
   """
   Returns the score of the player cards
   """

   # if black jack
   if sum(cards) == 21 and 11 in cards:
      return 0
   
   # if the sum of cards are greater than 21 and 11 in the cards
   elif sum(cards) > 21 and 11 in cards:
      cards.remove(11)
      cards.append(1)

   return sum(cards)

def compare(player_score, computer_score):
   results = {
      "draw": "Draw \n",
      "user_over": "You went over 21, Sorry! \n",
      "computer_over": "Computer went over 21, you win \n",
      "user_21": "You won with a blackjack! \n",
      "computer_21": "Sorry, computer had a blackjack",
      "user_win": "You win! \n",
      "user_lose": "You lose! \n"
   }
   if player_score == computer_score:
      ret = results["draw"]
   elif player_score > 21:
      ret = results["user_over"]
   elif computer_score > 21:
      ret = results["computer_over"]
   elif player_score == 0:
      ret = results["user_21"]
   elif computer_score == 0:
      ret = results["computer_21"]
   elif player_score > computer_score:
      ret = results["user_win"]
   else:
      ret = results["user_lose"]

   return ret

logo = """

.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \\/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \\  /|K /\\  |     | '_ \\| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \\/ | /  \\ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \\  / |     |_.__/|_|\\__,_|\\___|_|\\_\\ |\\__,_|\\___|_|\\_\\
      |  \\/ K|                            _/ |                
      `------'                           |__/      
"""

def game():
   print(logo)
   player_cards = [deal_cards() for _ in range(2)]
   computer_cards = [deal_cards() for _ in range(2)]
   game_continue = True
   while game_continue:
      player_score = calculate_score(player_cards)
      computer_score = calculate_score(computer_cards)

      print(f"Your cards are {player_cards} with current score {player_score}")
      time.sleep(2)
      print(f"Computer's first card is {computer_cards[0]}\n") 
      if player_score == 0 or computer_score == 0 or player_score > 21 or computer_score > 21:
         game_continue = False
      else:
         get_another_card = input("\nGet another card? (Y/N): ").lower()
         if get_another_card == "y":
            player_cards.append(deal_cards())
            player_score = calculate_score(player_cards)
         else:
            game_continue = False

   if player_score < 21 and computer_score != 0:
      while computer_score < player_score and computer_score < 17:
         computer_cards.append(deal_cards())
         computer_score = calculate_score(computer_cards)
   
   print(f"player final hand: {player_cards} with score {player_score}")
   time.sleep(2)
   print(f"Computer's final hand: {computer_cards} with score {computer_score}")
   time.sleep(2)
   print(compare(player_score = player_score, computer_score = computer_score))


print("Starting .....")
time.sleep(2)
clear_screen()

while input("""
Choose a game to start or write n to exit ....\n
1- Froggy
2- Twenty One
3- Snake
------------
""").lower() == "twenty one":
   clear_screen()
   game()
else:
   print("Exiting ....")
