from util import *

def print_player_hand(hand, sum):
  cards = []
  for card in hand:
    cards.append(card["face"])
  # print(f'Your hand: {hand} - Your total is {sum}')
  print(f'Your hand: {cards} - Your total is {sum}')

def print_dealer_hand(hand, sum):
  cards = []
  for card in hand:
    cards.append(card["face"])
  # print(f'\nDealer\'s hand: {hand} - Dealer\'s total is {sum}')
  print(f'\nDealer\'s hand: {cards} - Dealer\'s total is {sum}')

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