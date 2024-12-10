from board import Board
from player import Player
import game as g_

players: list[Player] = []
boards = []

def regNewPlayer():
  newPlayer = Player(input("Insira seu nome: "))
  players.append(newPlayer)

def chosePlayers(): 
  for i,v in enumerate(players):
      print(f"{i} - {v.name}")
    
  while True: 
    
    try: 
      p1 = int(input("Insira o id do jogador: ")) 
      if p1 < len(players):
        break  
    except ValueError:
      print("O seu burro, é numero!")
      
  while True: 
    try: 
      p2 = int(input("Insira o id do jogador: ")) 
      if p2 < len(players):
        break  
    except ValueError:
      print("O seu burro, é numero!")

  return players[p1], players[p2]
  
def newGame():
  isPlaying = chosePlayers()
  newBoard = Board(isPlaying[0], isPlaying[1])
  whoWon = g_.game(isPlaying, newBoard)
  
  print(f"O jogador {whoWon.name} ganhou!")
  boards.append(newBoard)

  

def main():
  while True:
    
    match input("1: Cadastrar novo jogador\n2: Nova Partida\n3: Ver Jogos\n4: Sair\n> "):
      case "1":
        regNewPlayer()

      case "2":
        newGame()

      case "3":
        for i,v in enumerate(boards):
            boardMatch = v.get_BoardMatch()
            print(f"{i} - {boardMatch[1].name} vs {boardMatch[2].name}\n Winner: {boardMatch[0]}")
        
      case "4":
        print("saindo do jogo...")
        break
        
      case _:
        print("Escolha errada amigão")

main()
