from antlr4 import *
from RationalNumbersLexer import RationalNumbersLexer
from RationalNumbersParser import RationalNumbersParser
from RationalNumbersListener import RationalNumbersListener

# Listener para evaluar las operaciones
class RationalEvalListener(RationalNumbersListener):
    def __init__(self):
        self.stack = []  # Pila para almacenar los resultados parciales

    # Al salir de una operación de suma o resta
    def exitAddSub(self, ctx):
        right = self.stack.pop()
        left = self.stack.pop()
        if ctx.op.type == RationalNumbersParser.PLUS:
            result = self.add_fractions(left, right)
        elif ctx.op.type == RationalNumbersParser.MINUS:
            result = self.subtract_fractions(left, right)
        self.stack.append(result)

    # Al salir de una operación de multiplicación o división
    def exitMulDiv(self, ctx):
        right = self.stack.pop()
        left = self.stack.pop()
        if ctx.op.type == RationalNumbersParser.MULT:
            result = self.multiply_fractions(left, right)
        elif ctx.op.type == RationalNumbersParser.DIV:
            result = self.divide_fractions(left, right)
        self.stack.append(result)

    # Al salir de una fracción
    def exitFraction(self, ctx):
        numerator = int(ctx.NUM(0).getText())
        denominator = int(ctx.NUM(1).getText())
        if denominator == 0:
            raise ZeroDivisionError("El denominador no puede ser cero.")
        self.stack.append((numerator, denominator))

    # Operaciones matemáticas con fracciones
    def add_fractions(self, left, right):
        return (left[0] * right[1] + right[0] * left[1], left[1] * right[1])

    def subtract_fractions(self, left, right):
        return (left[0] * right[1] - right[0] * left[1], left[1] * right[1])

    def multiply_fractions(self, left, right):
        return (left[0] * right[0], left[1] * right[1])

    def divide_fractions(self, left, right):
        if right[0] == 0:
            raise ZeroDivisionError("División por cero.")
        return (left[0] * right[1], left[1] * right[0])

# Función para simplificar fracciones
def simplify_fraction(numerator, denominator):
    from math import gcd
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor

# Función principal para evaluar las expresiones
def evaluate_expression(expression):
    input_stream = InputStream(expression)
    lexer = RationalNumbersLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = RationalNumbersParser(stream)

    try:
        tree = parser.expr()  # Analiza la expresión
        listener = RationalEvalListener()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)  # Recorre el árbol usando el listener

        # El resultado final estará en la cima de la pila del listener
        result = listener.stack.pop()
        return simplify_fraction(result[0], result[1])
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error de análisis: {e}")
        return None

# Ejecución principal
def main():
    expr = input("Ingrese la operación con números racionales: ")
    result = evaluate_expression(expr)

    if result:
        if result[1] == 1:
            print(f"Resultado: {result[0]}")
        else:
            print(f"Resultado: {result[0]}/{result[1]}")
    else:
        print("Error: La expresión no fue evaluada correctamente o hubo un error en la operación.")

if __name__ == "__main__":
    main()
