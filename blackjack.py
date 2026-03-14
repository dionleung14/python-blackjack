from random import randint
from logs import *

#   Game variables
upper_limit = 21
dealer_hit_limit = 16
card_limit = 13
game_start = True

card_mapper = {
  11: "J",
  12: "Q",
  13: "K"
}
# card_mapper = {
#   "11": "J",
#   "12": "Q",
#   "13": "K"
# }

# Deal one card
# TODO: account for 10, J, Q, K (if 10 or greater, make it 10)
# TODO: account for A being 1 or 11
def deal_card():
  return randint(1, card_limit)

# Deal one card with face cards
# TODO: account for A being 1 or 11
def deal_card_face():
  card_value = randint(1, card_limit)
  # if card_value != 1 and card_value < 11:
  if card_value < 11:
    return {"face": card_value, "value": card_value}
    # return card_value
  elif card_value >= 11:
    # letter = card_mapper[str(card_value)]
    letter = card_mapper[card_value]
    print(f"letter: {letter}")
    return {"face": letter, "value": 10}
    # return 10

def sum_hand(hand):
  sum = 0
  for card in hand:
    # sum += card.get("value")
    print("counting a card--------")
    print(card["value"])
    sum += card["value"]
    return sum

# Receive player action for replay
def get_play_again():
  decision = input("\nWould you like to play again (y/n)?: ")
  return decision

def end_game():
  print('\nThanks for playing!')

def play_another():
  print('\nPlaying again\n')
  print('Good luck!!\n')
  play_a_round([],[])

def handle_play_again(decision):
  if (decision.lower() == 'y'):
    play_another()
  elif (decision.lower() == 'n'):
    end_game()

# Receive player action for hit or stand
def get_hit_stand_decision():
  decision = input("\nWould you like to hit (h) or stand (s)?: ")
  return decision

# This is everything the dealer does when player stops playing
# Define it before player actions bc player actions calls this? What is Python's compilation order?
def dealers_actions(player_total, dealer_hit_limit, dealer_hand):
# if the dealer's total is 16 (hit limit) or less, must hit (repeat)
  while (sum(dealer_hand) <= dealer_hit_limit):
  # while (sum_hand(dealer_hand) <= dealer_hit_limit):
    print_dealer_hand(dealer_hand, sum(dealer_hand))
    # print_dealer_hand(dealer_hand, sum_hand(dealer_hand))
    print("Dealer must hit - New hand:")
    dealer_hand.append(deal_card())
    print_dealer_hand(dealer_hand, sum(dealer_hand))
    # print_dealer_hand(dealer_hand, sum_hand(dealer_hand))

# once the dealer's total breaks the hit limit (16), evaluate the end conditions:
# if the dealer's total is 22 or higher, the player wins
  if (sum(dealer_hand) > upper_limit):
  # if (sum_hand(dealer_hand) > upper_limit):
    print("Dealer busted - You WIN!")
    play_again = get_play_again()
    handle_play_again(play_again)

# if the dealer's total is 17 or higher (already true since we've exited the while loop)
# but not more than 21 (already true since we've passed the first if-condition)
# compare the dealer's total to the player's total (win or loss)
  elif (sum(dealer_hand) > player_total):
  # elif (sum_hand(dealer_hand) > player_total):
    print("Dealer has more than the player")
    print(f"Dealer's total = {sum(dealer_hand)}, player total = {player_total}")
    # print(f"Dealer's total = {sum_hand(dealer_hand)}, player total = {player_total}")
    print("You LOSE")
    play_again = get_play_again()
    handle_play_again(play_again)
  
  elif (sum(dealer_hand) < player_total):
  # elif (sum_hand(dealer_hand) < player_total):
    print("You have more than the Dealer")
    print(f"Dealer's total = {sum(dealer_hand)}, player total = {player_total}")
    # print(f"Dealer's total = {sum_hand(dealer_hand)}, player total = {player_total}")
    print("You WIN")
    play_again = get_play_again()

  # Lastly, compare a tie (can this be an else and not elif?)
  elif (sum(dealer_hand) == player_total):
  # elif (sum_hand(dealer_hand) == player_total):
    print("Tie game!")
    play_again = get_play_again()
    handle_play_again(play_again)


# This controls the player's actions
def players_actions(player_hand, dealer_hand):
# player is provided option to either hit or stand
  decision = get_hit_stand_decision()

# if hit
  if decision.lower() == 'h':
    print_player_hand(player_hand, sum(player_hand))
    # print_player_hand(player_hand, sum_hand(player_hand))
    print("You chose to HIT - New hand:")
#   player gets dealt 1 card
    player_hand.append(deal_card())
    print_player_hand(player_hand, sum(player_hand))
    # print_player_hand(player_hand, sum_hand(player_hand))

# if the total is 20 or less
# player is again provided option to either hit or stand (repeat (recursion, not while loop))
    if (sum(player_hand) <= upper_limit-1):
    # if (sum_hand(player_hand) <= upper_limit-1):
      players_actions(player_hand, dealer_hand)

# if the total is exactly 21, player wins
# TODO: allow for dealer to tie? aka go through dealer actions
    elif (sum(player_hand) == upper_limit):
    # elif (sum_hand(player_hand) == upper_limit):
      print("You WIN")
      play_again = get_play_again()
      handle_play_again(play_again)
    
# if the total is over 21, player loses
# TODO: allow for dealer to go through dealer actions?
    elif (sum(player_hand) > upper_limit):
    # elif (sum_hand(player_hand) > upper_limit):
      print("You lose, you BUSTED")
      play_again = get_play_again()
      handle_play_again(play_again)
    
    
# if stand, call the dealer's actions
  if decision.lower() == 's':
    summarize_stand_decision(player_hand, dealer_hand)

    print("\nDealer's actions\n")
    dealers_actions(sum(player_hand), dealer_hit_limit, dealer_hand)
    # dealers_actions(sum_hand(player_hand), dealer_hit_limit, dealer_hand)


def play_a_round(player_hand, dealer_hand):
  #   player gets dealt 2 cards
  player_hand.append(deal_card())
  player_hand.append(deal_card())

  #   dealer gets dealt 2 cards
  # TODO: hide one card from the Dealer
  dealer_hand.append(deal_card())
  dealer_hand.append(deal_card())

  # print(player_hand)

  # ptotal = sum_hand(player_hand)
  # print(ptotal)

  print_player_hand(player_hand, sum(player_hand))
  # print_player_hand(player_hand, sum_hand(player_hand))
  print_dealer_hand(dealer_hand, sum(dealer_hand))
  # print_dealer_hand(dealer_hand, sum_hand(dealer_hand))


  #   player's actions
  players_actions(player_hand, dealer_hand)


print_rules(upper_limit, dealer_hit_limit)

# Start a round with empty hands
play_a_round([],[])