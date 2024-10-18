grammar RationalNumbers;

// Reglas del parser
expr    : expr op=(PLUS|MINUS) term    # AddSub
        | term                         # ToTerm
        ;

term    : term op=(MULT|DIV) factor    # MulDiv
        | factor                       # ToFactor
        ;

factor  : rational                     # RationalNumber
        | '(' expr ')'                 # Parentheses
        ;

rational: NUM '/' NUM                  # Fraction
        ;

// Reglas del lexer
NUM     : [0-9]+ ;                     // Números enteros
PLUS    : '+' ;                        // Operador suma
MINUS   : '-' ;                        // Operador resta
MULT    : '*' ;                        // Operador multiplicación
DIV     : '/' ;                        // Operador división
LPAREN  : '(' ;                        // Paréntesis izquierdo
RPAREN  : ')' ;                        // Paréntesis derecho
WS      : [ \t\r\n]+ -> skip ;         // Ignorar espacios en blanco
