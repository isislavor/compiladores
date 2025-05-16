from Consts import Consts
from Token import Token
from Error import Error
class Lexer:
  def __init__(self, source_code) -> None:
    self.code = source_code
    self.current = None
    self.indice, self.coluna, self.linha = -1, -1, 0
    self.__advance()

  def __advance(self):
    self.__advanceCalc()
    self.current = self.code[self.indice] if self.indice < len(self.code) else None

  def __advanceCalc(self):
    self.indice += 1
    self.coluna += 1
    if self.current == '\n': 
      self.coluna = 0
      self.linha += 1      
    return self

  def makeTokens(self):
    tokens = []
    while self.current != None:
      if self.current in ' \t':
        self.__advance()
      if self.current == Consts.PLUS:
        tokens.append(Token(Consts.PLUS,Consts.PLUS))  
        self.__advance()
      elif self.current in Consts.DIGITOS + '.':
        tokens.append(self.makeNumber())
      else:
        return tokens, Error("Erro léxico")
    tokens.append(Token(Consts.EOF))
    return tokens, None

  def makeNumber(self):
    num_str = ''
    dot_count = 0
    start_col = self.coluna

    while self.current is not None and (self.current.isdigit() or self.current == '.'):
        if self.current == '.':
            if dot_count == 1: break
            dot_count += 1 
            num_str += '.'
        else:
            num_str += self.current
        self.__advance()
    if dot_count == 0:
        return Token(Consts.INT, int(num_str))
    else:
          return Token(Consts.FLOAT, float(num_str))             