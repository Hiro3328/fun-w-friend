import os
import gameLogic as _gl

def clearTerminal():
  os.system('cls||clear')


def showBoard(status: list[list], nome):
  # clearTerminal()

  print(f"""Vez do: {nome}
  
      A | B | C
  1 | {status[0][0]} | {status[0][1]} | {status[0][2]}
  2 | {status[1][0]} | {status[1][1]} | {status[1][2]}
  3 | {status[2][0]} | {status[2][1]} | {status[2][2]}""")


def game(players, board):
  turn = 0 
  players[0].set_symbol("X")
  players[1].set_symbol("O")
  
  while True:
    nowPlaying = players[turn]
    showBoard(board.get_boardStatus(), nowPlaying.name)

    try: 
        col, row = input("Insira a posição: ").upper()
        col, row = "ABC".index(col), "123".index(row)
        if board.get_boardStatus()[row][col] not in "XO":
            board.update_board(row, col, nowPlaying.get_symbol())
        turn = (turn+1)%2
    except (ValueError, IndexError) as e:
        print(e)

    

    if _gl.hasGameEnded(board.get_boardStatus(), nowPlaying):
      nowPlaying.update_score()
      return nowPlaying
