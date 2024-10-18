from LaplaceListener import LaplaceListener
from LaplaceParser import LaplaceParser

class MyLaplaceListener(LaplaceListener):

    def __init__(self):
        self.result = ""  # Aquí almacenamos el resultado final
        self.current_factor = []  # Almacenar cada factor de la multiplicación

    # Función llamada al entrar en una integral (LaplaceTransform)
    def enterLaplaceTransform(self, ctx: LaplaceParser.LaplaceTransformContext):
        self.result += "Transformada de Laplace: "

    # Función llamada al salir de la integral (cuando termina la regla)
    def exitLaplaceTransform(self, ctx: LaplaceParser.LaplaceTransformContext):
        # Combinar todos los factores multiplicados
        self.result += " * ".join(self.current_factor) + " dt"
        self.current_factor = []  # Limpiar la lista para futuros usos

    # Para manejar el término exponencial e^(-2 * t)
    def exitExpFactor(self, ctx: LaplaceParser.ExpFactorContext):
        base = ctx.getChild(4).getText()  # Obtener la base (por ejemplo, 2 o s)
        self.current_factor.append(f"1/(s + {base})")  # Transformada de e^(-at)

    # Para manejar la función seno sin(4 * t)
    def exitSinFactor(self, ctx: LaplaceParser.SinFactorContext):
        number = ctx.NUMBER().getText()
        self.current_factor.append(f"{number}/(s^2 + {number}^2)")  # Transformada de sin(nt)

    # Para manejar funciones genéricas f(t)
    def exitFuncFactor(self, ctx: LaplaceParser.FuncFactorContext):
        self.current_factor.append("F(s)")  # Transformada de f(t)

    # Para manejar multiplicaciones
    def exitMulExpr(self, ctx: LaplaceParser.MulExprContext):
        pass  # La multiplicación se maneja al final
