grammar MAPFilterFunction;

program : (mapExpr | filterExpr) EOF;

mapExpr : 'MAP' '(' functionOrIdentifier ',' iterable ')' ;  // Soporte para MAP
filterExpr : 'FILTER' '(' functionOrIdentifier ',' iterable ')' ;  // Soporte para FILTER

functionOrIdentifier : function | IDENTIFIER ;  // Aceptar una expresión lambda o una función existente

function : 'lambda' paramList ':' expr ;  // Expresión lambda

paramList : IDENTIFIER (',' IDENTIFIER)* ; // Parámetros de la función lambda

iterable : list | tuple | dict | rangeFunc | methodCall ;  // Soporte para listas, tuplas, diccionarios y llamadas a métodos

list : '[' (value (',' value)*)? ']' ;  // Definición de listas
tuple : '(' (value (',' value)*)? ')' ; // Definición de tuplas
dict : '{' (keyValuePair (',' keyValuePair)*)? '}' ;  // Definición de diccionarios
keyValuePair : value ':' value ;  // Par clave-valor de un diccionario

rangeFunc : 'range' '(' value (',' value (',' value)?)? ')' ;  // Soporte para range()

methodCall : IDENTIFIER '.' IDENTIFIER '(' ')' ;  // Llamadas a métodos como .keys() o .values()

value : NUMBER | IDENTIFIER | STRING ;  // Soporte para números, identificadores y strings

// Definición de expresiones aritméticas, lógicas y relacionales, incluyendo llamadas a métodos
expr : expr ('**' | '*' | '/' | '%' | '+' | '-') expr
     | expr ('>' | '<' | '>=' | '<=' | '==' | '!=') expr
     | expr ('and' | 'or') expr
     | 'not' expr
     | IDENTIFIER '.' IDENTIFIER '(' ')'  // Llamadas a métodos como .upper(), .lower()
     | '(' expr ')'
     | value;

STRING : '"' .*? '"' ;  // Soporte para cadenas de texto
NUMBER : [0-9]+ ;  // Soporte para números enteros
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]* ;  // Soporte para identificadores

WS : [ \t\r\n]+ -> skip ;  // Ignorar espacios en blanco
