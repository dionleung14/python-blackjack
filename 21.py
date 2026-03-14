'''
  game start
  player gets dealt 2 cards
  dealer gets dealt 2 cards

  player is provided option to either hit or stand
    if hit
      player gets dealt 1 card

      if the total is 20 or less
        player is again provided option to either hit or stand (repeat)

      if the total is 21 exactly
        skip to the dealer's actions
      
      if the total is 22 or higher
        end the game (player loss)

    if stand
      skip to the dealer's actions
  
      
  dealer's actions
    if the dealer's total is 16 or less
      must hit (repeat)
    
    if the dealer's total is 17 or higher but not more than 21
      compare the dealer's total to the player's total (win or loss)

    if the dealer's total is 22 or higher
      end the game (player win)

  '''



  

from random import randint
from logs import print_dealer_hand, print_player_hand

game_start = True
upper_limit = 15
dealer_hit_limit = 11
card_limit = 4
print('Enter "q" at any time to quit')

# def deal_card(face_up):
  # if face_up == True:
  #   return randint(0, 10)
  # else:
  #   value = randint(0, 10)
  #   return value  

def deal_card():
  return randint(1, card_limit)

def evaluate_player_bust(total, hand):
  if total > upper_limit:
    print_player_hand(hand, total)
    print('\nOh no you busted game over')
    return True
  else:
    return False
  
def evaluate_dealer_bust(total, hand):
  if total > upper_limit:
    print_dealer_hand(hand, total)
    print('\nThe Dealer busted, you win!')
    return True
  else:
    return False

# def new_game(phand,pbust,ptotal,dhand,dbust,dtotal):
# # def new_game(player_hand, player_bust, player_total, dealer_hand, dealer_bust, dealer_total):
#   print("starting new game")
#   phand = [deal_card(), deal_card()]
#   pbust = False
#   ptotal = 0
#   dhand = [deal_card(), deal_card()]
#   dbust = False
#   dtotal = 0


while game_start == True:

  player_hand = []
  player_bust = False
  player_total = 0

  dealer_hand = []
  dealer_bust = False
  dealer_total = 0

  round_start = True
  # new_game(player_hand, player_bust, player_total, dealer_hand, dealer_bust, dealer_total)
  while round_start == True:  
    print("\nStarting new round\n")

    player_hand.append(deal_card())
    player_hand.append(deal_card())
    player_total = sum(player_hand)
    dealer_hand.append(deal_card())
    dealer_hand.append(deal_card())
    dealer_total = sum(dealer_hand)


    ##### Player's actions
    while player_bust == False:
    # while player_bust == False and round_start == True:
      print("\nPlayer's actions")
      print_player_hand(player_hand, player_total)
      print_dealer_hand(dealer_hand, dealer_total)

      decision = input("\nWould you like to hit (h) or stand (s)?: ")

      # There has to be a better way to quit at this point
      if decision.lower() == 'q':
        # game_start = False
        # round_start = False
        # player_bust = True
        print('Thanks for playing')
        break
      
      if decision.lower() == 'h':
        player_hand.append(deal_card())
        player_total = sum(player_hand)
        player_bust = evaluate_player_bust(player_total, player_hand)
        if (player_bust == True):
          game_start = False
          round_start = False
          player_bust = True
          print('Thanks for playing')
          break

      if decision.lower() == 's':
        print("\nYou chose to STAND")
        print_player_hand(player_hand, player_total)

        print("\nTime for the dealer to play:")
        print_dealer_hand(dealer_hand, dealer_total)
        
        print("\nDealer's actions\n")
        ##### Dealer's actions
        while dealer_bust == False:
          if dealer_total < dealer_hit_limit:
            print(f"Dealer has less than {dealer_hit_limit}; Dealer must hit:")
            dealer_hand.append(deal_card())
            dealer_total = sum(dealer_hand)
            print_dealer_hand(dealer_hand, dealer_total)
            dealer_bust = evaluate_dealer_bust(dealer_total, dealer_hand)
          elif dealer_total >= dealer_hit_limit and dealer_total > player_total:
            print(f"\nDealer wins due to having more than {dealer_hit_limit} and more than player and not busting")
            print_dealer_hand(dealer_hand, dealer_total)
            print_player_hand(player_hand, player_total)
            dealer_bust == True # ends the game
            game_start = False
            break
          elif dealer_total >= dealer_hit_limit and dealer_total < player_total: 
            print(f"\nYou win! Dealer stands on {dealer_hit_limit}+:")
            dealer_total = sum(dealer_hand)
            print_dealer_hand(dealer_hand, dealer_total)
            print_player_hand(player_hand, player_total)
            round_start = False
            break
          elif dealer_total >= dealer_hit_limit and dealer_total == player_total: 
            print(f"\nPush (tie) game! Dealer stands on {dealer_hit_limit}+:")
            dealer_total = sum(dealer_hand)
            print_dealer_hand(dealer_hand, dealer_total)
            dealer_bust = evaluate_dealer_bust(dealer_total, dealer_hand)
            round_start = False
            break
          else:
            print("reached the else statement for dealer play")
            break

    continue
    #     play_again = input("Would you like to play again? (y/n): ")
    #     if play_again.lower() == 'y':
    #       print("playing again")
    #       player_hand.clear()
    #       dealer_hand.clear()
    #       break
    #     elif play_again.lower() == 'n':
    #       print("Thanks for playinnnnnnnnnnnnnn")
    #       game_start = False
    #       break
    #     elif play_again.lower() == 'q':
    #       game_start = False
    #       print('Thanks for playinggggggggggg')
    #       break
    # print("end of round start while loop")
    # play_again = input("Would you like to play again? (y/n): ")
    # if play_again.lower() == 'y':
    #   print("playing again")
    #   player_hand.clear()
    #   dealer_hand.clear()
    #   break
  print("end of game start while loop")