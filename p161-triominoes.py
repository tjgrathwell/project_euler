import copy
board = [[0,0,0,0] for x in xrange(6)]
pieces = [[[1,1],[1,0]],
         [[2,2],[0,2]],
         [[3,0],[3,3]],
         [[0,4],[4,4]],
         [[5],[5],[5]],
         [[6,6,6]]]
         
def printboard(board):
  for line in board:
    print line
         
def place(board, piece, top, left):
  for i in xrange(len(piece)):
    for j in xrange(len(piece[i])):
      if (piece[i][j] > 0):
        if (board[top+i][left+j]) != 0:
          return 0
        
  for i in xrange(len(piece)):
    for j in xrange(len(piece[i])):
      if (piece[i][j] > 0):
        board[top+i][left+j] = piece[i][j]
  return 1
       
def unplace(board, piece, top, left):
  for i in xrange(len(piece)):
    for j in xrange(len(piece[i])):
      if (piece[i][j] > 0):
        board[top+i][left+j] = 0
       
def is_full(board):
  for row in board:
    for col in row:
      if (col == 0):
        return 0
  return 1

def serialize(board):
  linear = [1]
  for row in board:
    linear += row
  return ''.join(str(c) for c in linear)
  
def deadboard(board):
  for i, row in enumerate(board):
    for j, col in enumerate(row):
      if col == 0:
        if (j == 0) or (board[i][j-1] != 0):
          if (i == 0) or (board[i-1][j] != 0):
            if (j == len(row)-1) or (board[i][j+1] != 0):
              if (i == len(board)-1) or (board[i+1][j] != 0):
                return 1
  return 0
  
seen_boards = {}
def placepieces(board, pieces):
  board_id = serialize(board)
  if board_id in seen_boards:
    return 0
    
  if deadboard(board):
    return 0

  if is_full(board):
    seen_boards[board_id] = 1
    return 1

  sum = 0
  for piece in pieces:
    for i in xrange(len(board)-len(piece)+1):
      for j in xrange(len(board[0])-len(piece[0])+1):
        place_result = place(board, piece,i,j)
        if (place_result != 0):
          sum += placepieces(board,pieces)
          unplace(board, piece, i, j)
  seen_boards[board_id] = sum
  return sum
      
def main():
  import time
  start = time.time()      
  print placepieces(board,pieces)
  print 'took ' + str(time.time() - start)

if __name__ == '__main__':
  import psyco, re
  psyco.profile(.03) #  Optimize any function taking over 3% of time
  main()

# almost right... so slow
# for sample:
# 9s without deadboard
# 3.6s with