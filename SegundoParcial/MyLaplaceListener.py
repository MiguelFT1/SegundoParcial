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
        self.current_factor.append("1/(s + " + ctx.NUMBER().getText() + ")")  # Transformada de e^(-at)

    # Para manejar la función genérica f(t)
    def exitFuncFactor(self, ctx: LaplaceParser.FuncFactorContext):
        self.current_factor.append("F(s)")  # Transformada de f(t)

    # Para manejar multiplicaciones
    def exitMulExpr(self, ctx: LaplaceParser.MulExprContext):
        pass  # No hacemos nada, la multiplicación se maneja al final con `*`

    # Para manejar números (en este caso no lo necesitamos para este ejemplo)
    def exitNumberFactor(self, ctx: LaplaceParser.NumberFactorContext):
        self.current_factor.append(ctx.NUMBER().getText())
