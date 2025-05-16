'''
REPL (Read-Eval-Print Loop) é um laço interativo que permite ao usuário digitar 
comandos, avaliá-los em tempo real, exibir os resultados e repetir o processo 
continuamente. É muito usado em linguagens interpretadas para testar e depurar
código de forma dinâmica, linha por linha. 
'''
from cmd import Cmd
from Lexer import Lexer

class Repl(Cmd):
    prompt = 'UFC> '
    intro = "Bem vindo!\nDigite\n :h para ajuda\n :q para sair e imprimir o assembly\n :s para um exemplo!"

    def do_exit(self, inp):
        return True
    def help_exit(self):
        print('Digite\n :q para sair\n :s para um exemplo!')
        return False
    def emptyline(self): # Desabilita repeticao do ultimo comando
        pass

    def default(self, linha): # cada linha do prompty cai aqui
        if linha == ':q':
            return self.do_exit(linha)
        elif linha == ':h':
            return self.help_exit()
        elif linha == ':s':
            return self.do_s()

        # Gerar tokens
        print(f'Linha digitada: {linha}')

        lexer = Lexer(linha)
        tokens, error = lexer.makeTokens()
        if error:
            print(f'Log de Erro: {error.printMsg()}')

        print(f'Lexer: {tokens}')

        return False

    def do_s(self):
        print("num = 10")

    do_EOF = do_exit
    help_EOF = help_exit