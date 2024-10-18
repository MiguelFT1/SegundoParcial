grammar Laplace;

PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
LPAREN: '(';
RPAREN: ')';
INTEGRAL: 'int';
EXP: 'e';
SIN: 'sin';
LIMIT_FROM: '0';
LIMIT_TO: 'infinity';
ID: [a-zA-Z]+;
NUMBER: [0-9]+ ('.' [0-9]+)?;
WS: [ \t\r\n]+ -> skip;

// Definición de la expresión principal
expr
    : integral               # LaplaceTransform
    | expr PLUS term          # AddExpr
    | expr MINUS term         # SubExpr
    | term                    # TermExpr
    ;

term
    : term MUL factor         # MulExpr
    | term DIV factor         # DivExpr
    | factor                  # FactorExpr
    ;

factor
    : NUMBER                  # NumberFactor
    | EXP '^' LPAREN MINUS (NUMBER | ID) MUL ID RPAREN   # ExpFactor // e^(-s * t) o e^(-2 * t)
    | SIN LPAREN NUMBER MUL ID RPAREN                    # SinFactor // sin(4 * t)
    | ID LPAREN expr RPAREN    # FuncFactor  // f(t)
    | ID                      # VariableFactor
    | LPAREN expr RPAREN       # ParenExpr
    ;

// La integral ahora permite más combinaciones explícitas de factores con números
integral
    : INTEGRAL LIMIT_FROM LIMIT_TO factor (MUL factor)* 'dt'  // Combinación de múltiples factores antes de 'dt'
    ;
