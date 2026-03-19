from util import *

next_card = "None; this is the last card"

def print_player_hand(hand, sum):
  player_cards = []
  for card in hand:
    player_cards.append(card["face"])
  # print(f'Your hand: {hand} - Your total is {sum}')
  print(f'Your hand: {player_cards} - Your total is {sum}')

def print_dealer_hand(hand, sum, display):
  dealer_cards = [] # Can this be a linked list...????
  for idx, card in enumerate(hand):
    if card["dealer_bool"] == True:
      if (idx < len(hand) - 1):
        card["next"] = hand[ idx + 1 ]
      else:
        card["next"] = next_card
      dealer_cards.append(card)
  
  cards_to_display = []
  for idx, card in enumerate(dealer_cards):
    if card["next"] == next_card and display == False:
      cards_to_display.append( "***" )  
    else:
      cards_to_display.append(card["face"])

  if display == False:
    print(f'\nDealer\'s hand: {cards_to_display}  - Dealer\'s total is {sum - dealer_cards[1]["value"]}')
  else:
    print(f'\nDealer\'s hand: {cards_to_display}  - Dealer\'s total is {sum}')


def summarize_stand_decision(player_hand, dealer_hand):
  print("\nYou chose to STAND")
  print_player_hand(player_hand, sum_hand_face(player_hand))
  print("\nTime for the dealer to play:")
  # print_dealer_hand(dealer_hand, sum_hand_face(dealer_hand), display=False)

def print_rules(upper_limit, dealer_hit_limit):
  print("Let's play Blackjack!")
  print(f"The Dealer must hit on {dealer_hit_limit} or less")
  print(f"(We're working on getting the dealer to hit on soft {dealer_hit_limit + 1})")
  print(f"Get as close as you can to {upper_limit} without going over!")
  print("Good luck!\n")