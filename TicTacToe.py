from enum import Enum
class TicTacToe:
  
  class STATES(Enum):
    CROSS_TURN = 0
    NAUGHT_TURN = 1
    DRAW = 2
    CROSS_WON = 3
    NAUGHT_WON = 4
    
  def __init__(self):
    self.n=3
    self.board=[[None for i in range(self.n)] for j in range(self.n)]
    self.xo=True
    
  def place_marker(self, symbol, row, column):
    if not self.board:
      raise Exception("GAME OVER")
    
    if not isinstance(symbol, str):
      raise TypeError("param 'symbol' must be of type 'str'")
    
    if not isinstance(row, int):
      raise TypeError("param 'row' must be of type 'int'")
    
    if not isinstance(column, int):
      raise TypeError("column must be of type 'int'")

    if symbol not in ['x', 'o']:
      raise Exception("Incorrect Symbol")
    
    if not 0<=row<len(self.board):
      raise Exception("Incorrect row index")
    
    if not 0<=column<len(self.board[0]):
      raise Exception("Incorrect column index")

    if self.board[row][column]:
      raise Exception("Cell occupied")

    if self.xo and symbol=="o":
      raise Exception("It's x's turn")

    if not self.xo and symbol=="x":
      raise Exception("It's o's turn")

    self.board[row][column]=symbol
    #self.display()

    if self.checkRow() or self.checkColumn() or self.checkDiagonal():
      self.board=None
      if self.xo:
        return self.STATES.CROSS_WON.value
      else:
        return self.STATES.NAUGHT_WON.value
    else:
      if self.checkDraw():
        return self.STATES.DRAW.value

      self.xo = not self.xo
      if self.xo:
        return self.STATES.CROSS_TURN.value
      else:
        return self.STATES.NAUGHT_TURN.value

  def checkDraw(self):
    for i in self.board:
      if all(i):
        continue
      else:
        return False
    else:
      return True

  def checkRow(self):
    for i in range(self.n):
      for j in range(self.n-1):
        if self.board[i][j] and self.board[i][j]==self.board[i][j+1]:
          continue
        else:
          break
      else:
        return True
    else:
      return False

  def checkColumn(self):
    for i in range(self.n):
      for j in range(self.n-1):
        if self.board[j][i] and self.board[j][i]==self.board[j+1][i]:
          continue
        else:
          break
      else:
        return True
    else:
      return False

  def checkDiagonal(self):
    for i in range(self.n-1):
        if self.board[i][i] and self.board[i][i]==self.board[i+1][i+1]:
          continue
        else:
          break
    else:
      return True
    
    for i in range(self.n-1):
        if self.board[i][self.n-1-i] and self.board[i][self.n-1-i]==self.board[i+1][self.n-1-i-1]:
          continue
        else:
          break
    else:
      return True

    return False

  def display(self):
    for row in self.board:
      for cell in row:
        print(" "+ cell, end=" ") if cell else print(" -", end=" ")
      print()