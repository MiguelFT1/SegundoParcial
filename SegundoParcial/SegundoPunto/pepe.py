
from MAPFilterFunctionLexer import MAPFilterFunctionLexer
from MAPFilterFunctionParser import MAPFilterFunctionParser
from antlr4 import *

# Definición de la función condicional 'multiple'
def multiple(x):
    return x % 2 == 0  # Filtra solo los múltiplos de 2

# Función que toma el árbol parseado y extrae la función lambda o el identificador de función
def extract_function(ctx):
    if ctx.mapExpr():  # Verificamos si es una expresión MAP
        func_ctx = ctx.mapExpr().functionOrIdentifier()
    elif ctx.filterExpr():  # Verificamos si es una expresión FILTER
        func_ctx = ctx.filterExpr().functionOrIdentifier()
    else:
        raise ValueError("No se pudo encontrar una expresión MAP o FILTER válida.")
    
    # Si es una función lambda
    if func_ctx.function():
        function_param = func_ctx.function().paramList().IDENTIFIER(0).getText()  # x en "lambda x:"
        function_body = func_ctx.function().expr().getText()  # "x.upper()" o "x * 2"
        
        # Agregar espacios entre operadores lógicos y relacionales
        function_body = function_body.replace('and', ' and ')
        function_body = function_body.replace('or', ' or ')
        function_body = function_body.replace('not', ' not ')
        function_body = function_body.replace('>', ' > ')
        function_body = function_body.replace('<', ' < ')
        function_body = function_body.replace('>=', ' >= ')
        function_body = function_body.replace('<=', ' <= ')
        function_body = function_body.replace('==', ' == ')
        function_body = function_body.replace('!=', ' != ')
        
        return f"lambda {function_param}: {function_body}"
    
    # Si es un identificador de función como str, int, etc.
    elif func_ctx.IDENTIFIER():
        return func_ctx.IDENTIFIER().getText()  # Devuelve el nombre de la función (str, int, etc.)
    else:
        raise ValueError("No se pudo extraer una función válida.")

# Función que extrae el iterable (lista o tupla) del árbol
def extract_iterable(ctx):
    if ctx.mapExpr():
        iterable_text = ctx.mapExpr().iterable().getText()  # Extraemos el texto del iterable en MAP
    elif ctx.filterExpr():
        iterable_text = ctx.filterExpr().iterable().getText()  # Extraemos el texto del iterable en FILTER
    else:
        raise ValueError("No se pudo encontrar un iterable válido.")
    
    # Evaluar diccionarios con métodos como .keys() o .values()
    if ".keys()" in iterable_text:
        dict_text = iterable_text.split('.keys()')[0]  # Obtener la parte del diccionario
        iterable = eval(dict_text).keys()  # Evaluar el diccionario y extraer las claves
    elif ".values()" in iterable_text:
        dict_text = iterable_text.split('.values()')[0]  # Obtener la parte del diccionario
        iterable = eval(dict_text).values()  # Evaluar el diccionario y extraer los valores
    else:
        iterable = eval(iterable_text)  # Evaluamos el texto para convertirlo en una lista o tupla en Python
    
    return iterable

# Función que aplica la función MAP o FILTER sobre el iterable
def apply_map_or_filter_function(tree, function_code, iterable):
    func = eval(function_code)  # Evalúa la función lambda o función nativa
    if tree.mapExpr():  # Verificamos si es una expresión MAP
        return list(map(func, iterable))  # MAP: Aplica la función a cada elemento
    elif tree.filterExpr():  # Verificamos si es una expresión FILTER
        return list(filter(func, iterable))  # FILTER: Filtra los elementos según la condición
    else:
        raise ValueError("No se pudo aplicar MAP o FILTER.")

def main():
    user_input = input("Introduce la expresión MAP o FILTER (por ejemplo, MAP(lambda x: x * 2, [1, 2, 3])):\n")
    
    # Analizamos la entrada con ANTLR
    input_stream = InputStream(user_input)
    lexer = MAPFilterFunctionLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MAPFilterFunctionParser(stream)
    tree = parser.program()  # Parseamos la entrada

    # Extraemos la función y el iterable desde el árbol
    function_code = extract_function(tree)
    iterable = extract_iterable(tree)

    # Aplicamos la función MAP o FILTER sobre el iterable
    result = apply_map_or_filter_function(tree, function_code, iterable)
    print(f"Resultado: {result}")

if __name__ == '__main__':
    main()
