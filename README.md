# compiladores
# 🧠 Simulador de Compilador em Python

Este é um projeto educacional desenvolvido para simular as etapas iniciais de um compilador, com foco em **análise léxica** e **análise sintática** por meio de um **parser recursivo descendente**. Implementado inteiramente em Python, ele permite interpretar instruções simples escritas em uma linguagem de programação fictícia, inspirada em estruturas comuns como variáveis, operações matemáticas, condicionais e expressões.

## 📌 Funcionalidades

- ✅ **Analisador léxico (Lexer)** com suporte a:
  - Números inteiros e reais
  - Strings com escape (`\n`, `\t`)
  - Operadores: `+`, `-`, `*`, `/`, `^`, `=`
  - Parênteses `()`, colchetes `[]`, vírgulas
  - Identificadores e palavras-chave (`let`, `if`, `while`, `null`, etc.)

- ✅ **Parser recursivo** com:
  - Análise sintática descendente (recursive descent)
  - Detecção e report de erros de sintaxe(Em construção)
  - Geração de árvore sintática abstrata (AST) (Em construção)

- ✅ **REPL interativo (Read-Eval-Print Loop)**
  - Interprete simples via terminal
  - Comandos especiais: `:h` (ajuda), `:q` (sair), `:s` (exemplo)

## ▶️ Como Executar

Clone o repositório e execute o programa com os comandos abaixo:

git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
pip install -r requirements.txt
python compilador/main.py

## 💡 Exemplos de Entrada

let x = 5 + 3 * (2 ^ 2)
let nome = "teste\nok"
if x > 10 {
    print(x)
}


## 📚 Aprendizados

Este projeto foi desenvolvido com fins didáticos, permitindo explorar:

* A construção de **analisadores léxicos manuais**
* A criação de **parsers recursivos** simples
* A arquitetura modular de **compiladores reais**
* A importância do tratamento de erros robusto

## 🚀 Próximos Passos

* [ ] Suporte a mais operadores lógicos (`==`, `!=`, `<=`, `>=`)
* [ ] Interpretação e execução da AST
* [ ] Geração de código intermediário ou "assembly" simulado
* [ ] Mais testes automatizados

## 👨‍💻 Autora

> Feito com 💻,🧠 e 🫀 por Isis Lavor estudante de Ciência da Computação (UFC - Campus Russas)
Com base no código fonte disponibilizado pelo Prof.Dr. Cenez de Araújo Rezende - UFC  
