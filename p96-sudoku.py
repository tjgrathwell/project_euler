import copy

def make_puzzle(rubbish):
  puzzle = []
  for row in rubbish:
    puzrow = []
    for num in row:
      if (num == '0'):
        puzrow.append([1,2,3,4,5,6,7,8,9])
      else:
        puzrow.append([int(num)])
    puzzle.append(puzrow)
  return puzzle
  
def reduce_group(group):
  reduced = 0
  for n in group:
    if (len(n) == 1):
      for s in group:
        if (len(s) > 1):
          if (n[0] in s):
            s.remove(n[0])
            reduced = 1
  return reduced
          
def make_col_group(n_col, puz):
  return [puz[i][n_col] for i in xrange(9)]
  
def make_3x3_group(top, left, puz):
  return puz[top][left:left+3] + puz[top+1][left:left+3] + puz[top+2][left:left+3]
  
def make_3x3_groups(n_group, puz):
  if (0 <= n_group <= 2):
    return make_3x3_group(0, n_group*3, puz)
  elif (3 <= n_group <= 5):
    return make_3x3_group(3, (n_group-3)*3, puz)
  elif (6 <= n_group <= 8):
    return make_3x3_group(6, (n_group-6)*3, puz)

def valid_group(group):
  seen = {}
  for n in group:
    if len(n) == 1:
      if n[0] in seen:
        return 0
      seen[n[0]] = 1
  return 1
  
def valid(puzzle):
  if all([valid_group(row) for row in puzzle]):
    if all([valid_group(make_col_group(col, puzzle)) for col in xrange(9)]):
      if all([valid_group(make_3x3_groups(group, puzzle)) for group in xrange(9)]):
        return 1
  return 0
  
def fully_reduced_group(group):
  for n in group:
    if len(n) != 1:
      return 0
  return 1
    
def fully_reduced(puzzle):
  if all([fully_reduced_group(row) for row in puzzle]):
    if all([fully_reduced_group(make_col_group(col, puzzle)) for col in xrange(9)]):
      if all([fully_reduced_group(make_3x3_groups(group, puzzle)) for group in xrange(9)]):
        return 1
  return 0
    
def reduce_puzzle(puzzle):
  reduced = 0
  reduced |= any([reduce_group(row) for row in puzzle])
  reduced |= any([reduce_group(make_col_group(col, puzzle)) for col in xrange(9)])
  reduced |= any([reduce_group(make_3x3_groups(group, puzzle)) for group in xrange(9)])
  return reduced
    
dbug = open("debug.txt","w")
def print_puzzle(puzzle):
  for line in puzzle:
    print line
    
# 'guess': choose arbitrary numbers for any given group of un-solved numbers
# 'guess' on a valid puzzle must return the full puzzle solution.
# 'guess' on an invalid puzzle must return 0
def guess(puzzle):
  for i, row in enumerate(puzzle):
    for j, col in enumerate(row):
      if len(col) > 1:
        # must be exactly one of these, or we're barking down the wrong tree
        for choice in col:
          temp_puzzle = copy.deepcopy(puzzle)
          temp_puzzle[i][j] = [choice]
          while reduce_puzzle(temp_puzzle): pass
          
          # invalid puzzle: keep trying different arbitrary choices
          if (not valid(temp_puzzle)): continue
          
          # fully reduced, valid puzzle: we're done
          if (fully_reduced(temp_puzzle)): return temp_puzzle
          
          # not fully reduced: make another guess, based on this temp puzzle
          solution = guess(temp_puzzle)
          if solution: return solution
          else: continue
        return 0

puzzles = []
lines = open("sudoku.txt","r").readlines()
for i in xrange(50):
  puzzles.append(make_puzzle([line.strip() for line in lines[10*i+1:10*i+10]]))
  
digits = []
for i, puzzle in enumerate(puzzles):
  while reduce_puzzle(puzzle):
    pass

  if not (valid(puzzle) and fully_reduced(puzzle)):
    puzzle = guess(puzzle)
    
  digits.append(int(''.join([str(x[0]) for x in puzzle[0][:3]])))
  
print sum(digits)
  
# program takes about 25 seconds... a little too slow if you ask me!
# one speedup would be to do a 'chain-reduce' rather than continually doing reduce(); make it so every newly placed digit kills other digits like it