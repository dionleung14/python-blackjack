from util import *

def print_player_hand(hand, sum):
  player_cards = []
  for card in hand:
    player_cards.append(card["face"])
  # print(f'Your hand: {hand} - Your total is {sum}')
  print(f'Your hand: {player_cards} - Your total is {sum}')

def print_dealer_hand(hand, sum):
  dealer_cards = [] # Can this be a linked list...????
  for idx, card in enumerate(hand):
    if card["dealer_bool"] == True:
      print("dealing a card to the dealer")
      print(f"this is card number {idx + 1}")
      print("previous state: \n")
      print(card)

      # card["next"] = cards[ idx + 1 ] if cards[idx + 1] == True else None
      if (idx < len(hand) - 1):
        print(f"next exists, the index is {idx} and the length is {len(hand)}")
        card["next"] = hand[ idx + 1 ]
      else:
        print("next does not exist")
        card["next"] = "none to see"
      # card["next"] = hand[ idx + 1 ] if (0 <= idx < len(hand)) else "None"
      print("added next")
      print(card)
      # cards_to_display.append(card["face"])
      dealer_cards.append(card)
  # print(f'\nDealer\'s hand: {hand} - Dealer\'s total is {sum}')
  print("exited for loop")
  cards_to_display = [] # Can this be a linked list...????
  print(cards_to_display)
  for idx, card in enumerate(dealer_cards):
    if card["next"] == "none to see":
      cards_to_display.append( " * " )  
    else:
      cards_to_display.append(card["face"])

  print(f'\nDealer\'s hand: {cards_to_display}  - Dealer\'s total is {sum - dealer_cards[1]["value"]}')
  # print(f'\nDealer\'s hand: {cards_to_display if cards_to_display["next"] != None else " * * "} - Dealer\'s total is 511111111')

def summarize_stand_decision(player_hand, dealer_hand):
  print("\nYou chose to STAND")
  # print_player_hand(player_hand, sum(player_hand))
  print_player_hand(player_hand, sum_hand_face(player_hand))
  print("\nTime for the dealer to play:")
  # print_dealer_hand(dealer_hand, sum(dealer_hand))
  print_dealer_hand(dealer_hand, sum_hand_face(dealer_hand))

def print_rules(upper_limit, dealer_hit_limit):
  print("Let's play Blackjack!")
  print(f"The Dealer must hit on {dealer_hit_limit} or less")
  print(f"(We're working on getting the dealer to hit on soft {dealer_hit_limit + 1})")
  print(f"Get as close as you can to {upper_limit} without going over!")
  print("Good luck!\n")