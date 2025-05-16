from Consts import Consts 
from Token import Token 
from Error import Error 

class Lexer:
    def __init__(self, source_code):
        self.code = source_code
        self.current = None
        self.indice, self.coluna, self.linha = -1, -1, 0
        self.__advance()

    def __advance(self):
        self.indice += 1
        if self.indice < len(self.code):
            self.current = self.code[self.indice]

            if self.current == '\n':
                self.linha += 1
                self.coluna = 0
            else:
                self.coluna += 1
        else:
            self.current = None
            
        self.__advanceCalc(self.current)

# Só falta fazer os outros e entender o porquê da chamada do advanceCalc nesse método acima!!!!

    def __advanceCalc(self, _char=None):
        return self
    
    def makeTokens(self):
        tokens = []

        while self.current != None:
            if self.current in '\t':
                self.__advance()
            elif self.current.isdigit():
                tokens.append(self.__makeNumber())
            else:
                self.__advance()

        tokens.append(Token(Consts.EOF))
        return tokens, None

    def __makeNumber(self):
        num_str = ''
        dot_count = 0
        start_col = self.coluna

        while self.current is not None and (self.current.isdigit() or self.current == '.'):
            if self.current == '.':
                if dot_count == 1:
                    break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current
            
            self.__advance()
        if dot_count == 0:
            return Token(Consts.INT, int(num_str), self.linha, start_col)
        else:
             return Token(Consts.FLOAT, float(num_str), self.linha, start_col)              