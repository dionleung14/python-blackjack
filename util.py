def sum_hand_face(hand):
  sum = 0
  for card in hand:
    sum += card["value"]
  return sum

# Receive player action for hit or stand
def get_hit_stand_decision():
  decision = input("\nWould you like to hit (h) or stand (s)?: ")
  return decision
