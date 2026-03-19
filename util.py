def sum_hand_face(hand):
  sum = 0
  for card in hand:
    sum += card["value"]
  return sum

# def sum_hand_face(hand):
#   sum = 0
#   for card in hand:
#     sum += card["value"]
#   return sum
