# SegundoParcial

# Primer Punto
# Calculadora de Operaciones con Números Racionales

Este proyecto es una calculadora que realiza operaciones aritméticas básicas (suma, resta, multiplicación y división) con fracciones. El programa utiliza **ANTLR** para generar el lexer, el parser y el listener a partir de una gramática definida. Las fracciones se simplifican automáticamente después de cada operación, y se maneja la división por cero o fracciones mal formadas.

## Funcionalidades

- Soporta las operaciones aritméticas básicas con fracciones:
  - Suma: `(1/3 + 2/3)`
  - Resta: `(5/6 - 1/2)`
  - Multiplicación: `(2/3 * 3/4)`
  - División: `(1/2 / 1/4)`
  - Uso de paréntesis para modificar el orden de las operaciones: `((1/2 + 2/3) * (3/4 - 1/5))`
- Simplificación automática de las fracciones después de cada operación.
- Manejo de fracciones mal formadas (por ejemplo, evitando la división por cero).
- Manejo de errores de análisis sintáctico.

## Requisitos previos

### Instalación de ANTLR

1. **Instalar ANTLR**:
   Debes tener **ANTLR 4** instalado en tu sistema. Si aún no lo tienes, puedes descargarlo desde [la página oficial de ANTLR](https://www.antlr.org/).

   **Instalación en Linux/Mac**:
   ```bash
   curl -O https://www.antlr.org/download/antlr-4.13.2-complete.jar
   alias antlr4='java -jar antlr-4.13.2-complete.jar'
   alias grun='java org.antlr.v4.gui.TestRig'
   
2.Instalación en Windows: Descarga el archivo JAR desde ANTLR y asegúrate de tener Java instalado.

Instalar las dependencias en Python: Asegúrate de tener antlr4-python3-runtime instalado:

pip install antlr4-python3-runtime

## Generar el Lexer, Parser y Listener
Gramática: El archivo RationalNumbers.g4 define las reglas de gramática para las operaciones aritméticas con fracciones.

Generar archivos de ANTLR: Para generar el lexer, parser y listener, ejecuta el siguiente comando en el directorio donde se encuentra RationalNumbers.g4:
antlr4 -Dlanguage=Python3 -listener RationalNumbers.g4
Esto generará los archivos RationalNumbersLexer.py, RationalNumbersParser.py y RationalNumbersListener.py.

Cómo ejecutar el programa
Compila y ejecuta: Asegúrate de que has generado correctamente los archivos con ANTLR y que tienes Python configurado.

Ejecutar el programa: Para ejecutar la calculadora, simplemente ejecuta el archivo rational_calculator.py con Python:
python3 rational_calculator.py

Ingresar una operación: El programa te pedirá que ingreses una operación con fracciones. Por ejemplo:
Ingrese la operación con números racionales: (1/3 + 2/3)

Ejemplos de uso
Ejemplo 1: Suma de fracciones
Entrada:
(1/3 + 2/3)
Salida:
Resultado: 1

Ejemplo 2: División por cero
Entrada:
1/0
Salida:
Error: El denominador no puede ser cero.

Ejemplo 3: Expresión con paréntesis y operaciones combinadas
Entrada:Ejemplos de uso
Ejemplo 1: Suma de fracciones
Entrada:
bash
Copiar código
(1/3 + 2/3)
Salida:
bash
Copiar código
Resultado: 1
Ejemplo 2: División por cero
Entrada:
bash
Copiar código
1/0
Salida:
bash
Copiar código
Error: El denominador no puede ser cero.
Ejemplo 3: Expresión con paréntesis y operaciones combinadas
Entrada:
bash
Copiar código
((1/2 + 2/3) * (3/4 - 1/5))
Salida:
bash
Copiar código
Resultado: 77/180
((1/2 + 2/3) * (3/4 - 1/5))
Salida:
Resultado: 77/180


# Segundo Punto:
# Proyecto MAP & FILTER en Python usando ANTLR

Este proyecto permite aplicar funciones de `MAP` y `FILTER` a listas, tuplas, y diccionarios en Python. Utiliza **ANTLR** para analizar y procesar expresiones de tipo `MAP` y `FILTER` con funciones definidas por el usuario o funciones estándar, y ejecuta la lógica sobre objetos iterables.

## Características

- **MAP**: Aplica una función a cada elemento de un iterable y devuelve una nueva colección con los resultados.
- **FILTER**: Filtra los elementos de un iterable que cumplan con una condición dada por una función y devuelve una nueva colección con los elementos que cumplen la condición.
- **Soporte para diccionarios**: Se pueden usar métodos como `.keys()` y `.values()` en diccionarios.
- **Soporte para expresiones lambda y funciones estándar**: Puedes usar funciones `lambda` o funciones definidas como `str`, `int`, `multiple`, entre otras.

## Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener lo siguiente instalado:

1. **Python 3.x**: El lenguaje objetivo es Python.
2. **ANTLR 4**: Para generar el lexer y el parser a partir del archivo de gramática.
3. **Java**: ANTLR requiere Java para ejecutarse.

### Instalación de ANTLR

Si no tienes ANTLR instalado, sigue estos pasos:

1. Descarga el JAR de ANTLR desde [ANTLR Releases](https://www.antlr.org/download.html).
2. Agrega el JAR al `CLASSPATH`:

   ```bash
   export CLASSPATH=".:/path/to/antlr-4.x-complete.jar:$CLASSPATH"
   alias antlr4='java -jar /path/to/antlr-4.x-complete.jar'
   alias grun='java org.antlr.v4.gui.TestRig'

Estructura del Proyecto
MAPFilterFunction.g4: Archivo de gramática para ANTLR que define las reglas para reconocer las expresiones MAP y FILTER.

pepe.py: Script principal de Python que recibe las expresiones desde la consola, procesa el texto con el lexer y parser generados por ANTLR, y aplica las funciones MAP o FILTER al iterable.

MAPFilterFunctionLexer.py y MAPFilterFunctionParser.py: Archivos generados automáticamente por ANTLR a partir del archivo MAPFilterFunction.g4.

Uso
Paso 1: Generar el Lexer y el Parser
Antes de ejecutar el programa, debes generar el lexer y parser a partir de la gramática:

antlr4 -Dlanguage=Python3 MAPFilterFunction.g4
Este comando generará los archivos MAPFilterFunctionLexer.py y MAPFilterFunctionParser.py.

Paso 2: Ejecutar el Programa
Una vez generado el lexer y el parser, puedes ejecutar el programa principal pepe.py:

python3 pepe.py
El programa pedirá una expresión MAP o FILTER como:

Introduce la expresión MAP o FILTER (por ejemplo, MAP(lambda x: x * 2, [1, 2, 3])):

## En el archivo ejemplos.txt se encontraran una variedad de ejemplos que el programa puede utilizar.

# Tercer Punto:

Proyecto de Transformada de Laplace
Este proyecto implementa un analizador para calcular la Transformada de Laplace de expresiones matemáticas. Se utilizan gramáticas definidas en ANTLR para analizar expresiones como funciones exponenciales y trigonométricas, y generar su Transformada de Laplace en formato simbólico.

Estructura del Proyecto
El proyecto contiene los siguientes archivos principales:

Laplace.g4: Definición de la gramática de ANTLR para reconocer expresiones como 
𝑒−𝑎𝑡e −at , sin⁡(𝑛𝑡)
sin(nt), y funciones genéricas 𝑓(t).
LaplaceLexer.py y LaplaceParser.py: Archivos generados por ANTLR a partir de la gramática, que implementan el análisis léxico y sintáctico.
MyLaplaceListener.py: Implementación de un listener que maneja las transformadas de expresiones matemáticas.
Laplace.py: Script principal que recibe las expresiones, las analiza usando ANTLR y produce el resultado de la Transformada de Laplace.
Funcionalidad Principal
El proyecto soporta el análisis de las siguientes expresiones:

Funciones exponenciales: 
𝑒−𝑎𝑡e −at , donde 𝑎a puede ser un número o una variable.
Funciones trigonométricas: sin⁡(𝑛𝑡)sin(nt), donde 𝑛n es un número.
Funciones genéricas: 𝑓(𝑡)f(t), que se representarán como 𝐹(𝑠)
F(s) en la salida.
Operaciones básicas: suma, resta, multiplicación de términos.

Ejemplos de Entrada
El programa admite entradas de tipo integral para calcular la Transformada de Laplace, como los siguientes ejemplos:

Transformada de una función exponencial:

Entrada:
int 0 infinity e^(-s * t) * f(t) dt

El cual fue el ejemplo presentado el el documento y el resultado debe ser el siguiente:

Transformada de Laplace: 1/(s + s) * F(s) dt

hay mas ejempolos en el documento ejemplos para probar el programa


