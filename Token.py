class Token:
    def __init__(self, tipo, valor=None, linha=None, coluna=None):
        self.type = tipo
        self.value = valor
        self.linha = linha
        self.coluna = coluna

    def matches(self, _type, _value):
        return self.type == _type and self.value == _value

    def __repr__(self):
        pos_info = f' @L{self.linha},C{self.coluna}' if self.linha is not None else ''
        if self.value is not None:
            return f'{self.type}:{self.value}{pos_info}'
        return f'{self.type}{pos_info}' 