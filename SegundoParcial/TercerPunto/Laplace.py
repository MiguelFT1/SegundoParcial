import sys
from antlr4 import *
from LaplaceLexer import LaplaceLexer
from LaplaceParser import LaplaceParser
from MyLaplaceListener import MyLaplaceListener
from antlr4.tree.Tree import ParseTreeWalker

def main():
    try:
        # Lee la entrada desde el archivo o la consola
        input_stream = InputStream(input('? '))
        
        # Lexer
        lexer = LaplaceLexer(input_stream)
        stream = CommonTokenStream(lexer)
        
        # Parser
        parser = LaplaceParser(stream)
        tree = parser.expr()  # Inicia el análisis desde la regla expr

        # Conectamos el listener
        listener = MyLaplaceListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)

        # Mostramos el resultado
        print(listener.result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
