class Error:
    runTimeError = "RunTime Error"
    parserError = "Parser Error"
    lexerError = "Lexer Error"
    
    def __init__(self, msg):
        self.msg = msg
    
    def __repr__(self):
        return f'({self.msg})'

    def printMsg(self):
        return self