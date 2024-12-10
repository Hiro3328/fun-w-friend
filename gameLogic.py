# | sy sy sy | sy -- -- | -- sy -- | -- -- sy |
# | -- -- -- | -- sy -- | -- sy -- | -- sy -- |
# | -- -- -- | -- -- sy | -- sy -- | sy -- -- |

def rotate90deg(board):
  return [
    [
     value[rowId] 
     for value in board
    ] 
    for rowId in range(len(board))
  ]

def hasGameEnded(status, player) -> None | bool:
    cases = [
        [sum(i==player.get_symbol() for i in item) for item in status],
        [sum(i==player.get_symbol() for i in item) for item in rotate90deg(status)],
        [sum(status[i][i]==player.get_symbol() for i in range(3))],
        [sum(status[i][2-i]==player.get_symbol() for i in range(3))]
    ]

    for case in cases:
        if 3 in case:
            return True
    return False

