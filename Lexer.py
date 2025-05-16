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
        self.__advanceCalc(self.current)
        self.current = self.code[self.indice] if self.indice < len(self.code) else None

    def __advanceCalc(self, _char=None):
        self.indice += 1
        self.coluna += 1
        if self.current == '\n':
            self.coluna = 0
            self.linha += 1
        return self

    def makeTokens(self):
        tokens = []
        while self.current is not None:
            if self.current in ' \t':
                self.__advance()

            elif self.current == Consts.PLUS:
                tokens.append(Token(Consts.PLUS))
                self.__advance()

            elif self.current == Consts.MINUS:
                tokens.append(Token(Consts.MINUS))
                self.__advance()

            elif self.current == Consts.MUL:
                tokens.append(Token(Consts.MUL))
                self.__advance()

            elif self.current == Consts.DIV:
                tokens.append(Token(Consts.DIV))
                self.__advance()
            
            elif self.current == Consts.LPAR:
                tokens.append(Token(Consts.LPAR))
                self.__advance()

            elif self.current == Consts.RPAR:
                tokens.append(Token(Consts.RPAR))
                self.__advance()

            elif self.current == Consts.POW:
                tokens.append(Token(Consts.POW))
                self.__advance()

            elif self.current == Consts.EQ:
                tokens.append(Token(Consts.EQ))
                self.__advance()

            elif self.current == Consts.LSQUARE:
                tokens.append(Token(Consts.LSQUARE))
                self.__advance()

            elif self.current == Consts.RSQUARE:
                tokens.append(Token(Consts.RSQUARE))
                self.__advance()

            elif self.current == Consts.COMMA:
                tokens.append(Token(Consts.COMMA))
                self.__advance()  

            elif self.current in Consts.DIGITOS:
                tokens.append(self.__makeNumber())

            elif self.current == '"':
                string = self.__makeString()
                if self.current != '"':
                    return [], Error(f"{Error.lexerError}: expecting '\"'")
                self.__advance()
                tokens.append(string)

            elif self.current in Consts.LETRAS + Consts.UNDER:
                tokens.append(self.__makeID())

            else:
                return tokens, Error(f"{Error.lexerError}: caractere inválido '{self.current}'")

        tokens.append(Token(Consts.EOF))
        return tokens, None

    def __makeNumber(self):
        strNum = ''
        conta_ponto = 0
        while self.current is not None and self.current in Consts.DIGITOS + '.':
            if self.current == '.':
                if conta_ponto == 1:
                    break
                conta_ponto += 1
            strNum += self.current
            self.__advance()

        if conta_ponto == 0:
            return Token(Consts.INT, int(strNum))
        return Token(Consts.FLOAT, float(strNum))

    def __makeString(self):
        stri = ""
        bypass = False
        self.__advance()
        specialChars = {'n': '\n', 't': '\t'}
        while self.current is not None and (self.current != '"' or bypass):
            if bypass:
                c = specialChars.get(self.current, self.current)
                stri += c
                bypass = False
            else:
                if self.current == '\\':
                    bypass = True
                else:
                    stri += self.current
            self.__advance()
        return Token(Consts.STRING, stri)

    def __makeID(self):
        ident = ''
        while self.current is not None and (
            self.current in Consts.LETRAS + Consts.DIGITOS + Consts.UNDER
        ):
            ident += self.current
            self.__advance()
        if ident in Consts.KEYS:
            return Token(Consts.KEY, ident)
        return Token(Consts.ID, ident)
