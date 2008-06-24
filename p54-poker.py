hands = []
for line in open("poker.txt"):
  line = line.strip()
  hands.append((line.split(' ')[:5], line.split(' ')[5:]))
  
# note: no RFLUSH, SFLUSH in dataset
(HIGH, PAIR, TWOPAIR, THREEKIND, STRAIGHT, FLUSH, FULLHOUSE, FOURKIND, SFLUSH, RFLUSH) = range(10)
types = ('HIGH', 'PAIR', 'TWOPAIR', 'THREEKIND', 'STRAIGHT', 'FLUSH', 'FULLHOUSE', 'FOURKIND', '', '')
value_hash = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

def is_flush(hand):
  first = hand[0][1]
  for card in hand[1:]:
    if (card[1] != first):
      #print card[1], first
      return 0
  return 1
  
def is_straight(hand):
  values = [value_hash[card[0]] for card in hand]
  values.sort()
  last = values[0]
  for val in values[1:]:
    if (val != last+1):
      return 0
    last = val
  return 1
  
def hash_hand(hand):
  # first count how many of each card
  seen = {}
  for card in hand:
    if card[0] in seen:
      seen[card[0]] += 1
    else:
      seen[card[0]] = 1
  # then return the reversed hash: that is, lists of what cards in each value
  rethash = {}
  for card in seen:
    rethash.setdefault(seen[card],[]).append(card)
  return rethash
  
def classify(hand):
  hashed = hash_hand(hand)
  if 4 in hashed:
    return FOURKIND
  if (3 in hashed) and (4 in hashed):
    return FULLHOUSE
  if is_flush(hand):
    return FLUSH
  if is_straight(hand):
    return STRAIGHT
  if 3 in hashed:
    return THREEKIND
  if 2 in hashed:
    if len(hashed[2]) > 1:
      return TWOPAIR
    return PAIR
  return HIGH
  
# return ambiguous for cases of two pair, etc
def group_val(hand, group):
  return value_hash[hash_hand(hand)[group][0]]
  
def break_tie(hand1, hand2, rank):
  if (rank == FOURKIND):
    if (group_val(hand1,4) > group_val(hand2,4)):
      return 1
    elif (group_val(hand1,4) == group_val(hand2,4)):
      if (group_val(hand1,1) > group_val(hand2,1)):
        return 1
    return 0
    
  if (rank == FULLHOUSE):
    if (group_val(hand1,3) > group_val(hand2,3)):
      return 1
    elif (group_val(hand1,3) == group_val(hand2,3)):
      if (group_val(hand1,2) > group_val(hand1,2)):
        return 1
      elif (group_val(hand1,2) == group_val(hand1,2)):
        if (group_val(hand1,1) == group_val(hand1,1)):
          return 1
    return 0
    
  if (rank == FLUSH or rank == STRAIGHT or rank == HIGH):
    return max([value_hash[card[0]] for card in hand1]) > max([value_hash[card[0]] for card in hand2])
    
  if (rank == THREEKIND):
    if (group_val(hand1,3) > group_val(hand2,3)):
      return 1
    elif (group_val(hand1,3) == group_val(hand2,3)):
      return max([value_hash[card] for card in hash_hand(hand1)[1]]) > max([value_hash[card] for card in hash_hand(hand1)[1]])
    return 0
    
  if (rank == TWOPAIR):
    for (pair1,pair2) in zip(sorted(hash_hand(hand1)[2])[::-1],sorted(hash_hand(hand2)[2])[::-1]):
      if value_hash[pair1] > value_hash[pair2]:
        return 1
      if value_hash[pair1] < value_hash[pair2]:
        return 0
    return group_val(hand1,1) > group_val(hand2,1)
    
  if (rank == PAIR):
    if (group_val(hand1,2) > group_val(hand2,2)):
      return 1
    elif (group_val(hand1,2) == group_val(hand2,2)):
      return max([value_hash[card] for card in hash_hand(hand1)[1]]) > max([value_hash[card] for card in hash_hand(hand2)[1]])
    return 0
  
wins = 0
for game in hands:
  (p1score, p2score) = (classify(game[0]), classify(game[1]))
  print game
  print types[p1score], types[p2score],
  if p1score > p2score:
    wins += 1
    print 'p1'
  elif p1score == p2score:
    if break_tie(game[0],game[1],p1score):
      wins += 1
      print 'p1'
    else:
      print 'p2'
  else:
    print 'p2'

print wins