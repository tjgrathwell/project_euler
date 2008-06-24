values = [200, 100, 50, 20, 10, 5, 2, 1]
goal = 200

while (used_up < len(values)):
  coins = []
  for i in xrange(used_up, len(values)):
    while (sum(coins) + values[i]) <= goal:
      coins.append(values[i])
    if (sum(coins) == goal):
  