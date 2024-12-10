class Board:
  def __init__(self, player1, player2):
    self.__board = [ 
            ["_", "_", "_"], #0
            ["_", "_", "_"], #1
            ["_", "_", "_"]  #2
        ]#    A    B    C
    self.__whoWon = None
    self.__player1 = player1
    self.__player2 = player2

  def get_boardStatus(self):
    return self.__board

  def update_board(self, row, col, symbol):
    self.__board[row][col] = symbol
    
  def update_whoWon(self, player):
    self.__whoWon = player
    return 1
    
  def get_BoardMatch(self):
    return self.__whoWon, self.__player1, self.__player2

