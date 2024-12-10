class Player:
  __score = 0
  def __init__(self, name, symbol:None| str = None):
    self.name = name
    self.__symbol = symbol

  def get_symbol(self):
    return self.__symbol

  def set_symbol(self, symbol: str):
    if symbol in "XO":
      self.__symbol = symbol
    else:
      return -1 

  def update_score(self):
    self.__score += 1

  def get_score(self):
    return self.__score
