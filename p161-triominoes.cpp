#include<map>
#include<iostream>
#include<string>
#include<vector>
using namespace std;

#define ROWS 9
#define COLS 4

map<string,int> seen_boards;
vector<vector<vector<int> > > pieces;

void clearboard(int board[ROWS][COLS])
{
  for (int i = 0; i < ROWS; i++)
  {
    for (int j = 0; j < COLS; j++)
      board[i][j] = 0;
  }
}

void printboard(int board[ROWS][COLS])
{
  for (int i = 0; i < ROWS; i++)
  {
    for (int j = 0; j < COLS; j++)
      cout << board[i][j];
    cout << endl;
  }
}

bool deadboard(int board[ROWS][COLS])
{
  for (int i = 0; i < ROWS; i++)
  {
    for (int j = 0; j < COLS; j++)
    {
      if (board[i][j] == 0)
      {
        if (((j == 0) || (board[i][j-1] != 0)) &&
            ((i == 0) || (board[i-1][j] != 0)) &&
            ((j == COLS-1) || (board[i][j+1] != 0)) &&
            ((i == ROWS-1) || (board[i+1][j] != 0))) return 1;
      }
    }
  }
  return 0;
}

bool is_full(int board[ROWS][COLS])
{
  for (int i = 0; i < ROWS; i++)
    for (int j = 0; j < COLS; j++)
      if (board[i][j] == 0) return 0;
  return 1;
}
  
string serialize(int board[ROWS][COLS])
{
  string result;
  char c[1];
  for (int i = 0; i < ROWS; i++)
  {
    for (int j = 0; j < COLS; j++)
    {
      sprintf(c, "%d", board[i][j]);
      result.append(c);
    }
  }
  return result;
}
  
bool place(int board[ROWS][COLS], vector<vector<int> > piece, int top, int left)
{
  for (int i = 0; i < piece.size(); i++)
    for (int j = 0; j < piece[i].size(); j++)
      if ((piece[i][j] > 0) && ((board[top+i][left+j]) != 0)) return 0;
        
  for (int i = 0; i < piece.size(); i++)
    for (int j = 0; j < piece[i].size(); j++)
      if (piece[i][j] > 0)
        board[top+i][left+j] = piece[i][j];

  return 1;
}
 
bool unplace(int board[ROWS][COLS], vector<vector<int> > piece, int top, int left)
{
  for (int i = 0; i < piece.size(); i++)
    for (int j = 0; j < piece[i].size(); j++)
      if (piece[i][j] > 0)
        board[top+i][left+j] = 0;
}

int placepieces(int board[ROWS][COLS], vector<vector<vector<int> > > pieces)
{
  string board_id = serialize(board);
  map<string,int>::iterator iter = seen_boards.find(board_id);
  if( iter != seen_boards.end() ) {
    return 0;
  }
    
  if (deadboard(board))
    return 0;

  if (is_full(board))
  {
    seen_boards[board_id] = 1;
    return 1;
  }

  unsigned int sum = 0;
  for (int p = 0; p < pieces.size(); p++)
  {
    for (int i = 0; i < ROWS-pieces[p].size()+1; i++)
      for (int j = 0; j < COLS-pieces[p][0].size()+1; j++)
      {
        bool place_result = place(board, pieces[p],i,j);
        if (place_result != 0)
        {
          sum += placepieces(board,pieces);
          unplace(board, pieces[p], i, j);
        }
      }
  }
  seen_boards[board_id] = sum;
  return sum;
}
  
int main()
{
  vector<vector<int> > p1(2);
  vector<int> p11(2); p11[0] = 1; p11[1] = 1;
  vector<int> p12(2); p12[0] = 1; p12[1] = 0;
  p1[0] = p11; p1[1] = p12;
  pieces.push_back(p1);

  vector<vector<int> > p2(2);
  vector<int> p21(2); p21[0] = 2; p21[1] = 2;
  vector<int> p22(2); p22[0] = 0; p22[1] = 2;
  p2[0] = p21; p2[1] = p22;
  pieces.push_back(p2);
  
  vector<vector<int> > p3(2);
  vector<int> p31(2); p31[0] = 3; p31[1] = 0;
  vector<int> p32(2); p32[0] = 3; p32[1] = 3;
  p3[0] = p31; p3[1] = p32;
  pieces.push_back(p3);
  
  vector<vector<int> > p4(2);
  vector<int> p41(2); p41[0] = 0; p41[1] = 4;
  vector<int> p42(2); p42[0] = 4; p42[1] = 4;
  p4[0] = p41; p4[1] = p42;
  pieces.push_back(p4);
  
  vector<vector<int> > p5(3);
  vector<int> p51(1,5); vector<int> p52(1,5); vector<int> p53(1,5);
  p5[0] = p51; p5[1] = p52; p5[2] = p53;
  pieces.push_back(p5);
  
  vector<vector<int> > p6(1);
  vector<int> p61(3,6);
  p6[0] = p61;
  pieces.push_back(p6);

  int board[ROWS][COLS];

  clearboard(board);
  time_t stime;
  time(&stime);
  cout << ROWS << "x" << COLS << ": " << placepieces(board,pieces) << endl;
  time_t etime;
  time(&etime);
  cout << "took " << etime - stime << " seconds" << endl;
}

/*
import copy
board = [[0,0,0,0] for x in xrange(6)]
pieces = [[[1,1],[1,0]],
         [[2,2],[0,2]],
         [[3,0],[3,3]],
         [[0,4],[4,4]],
         [[5],[5],[5]],
         [[6,6,6]]]
         
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
  main()

# almost right... so slow
# for sample:
# 9s without deadboard
# 3.6s with
*/
