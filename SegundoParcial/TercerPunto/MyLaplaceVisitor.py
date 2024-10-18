from LaplaceVisitor import LaplaceVisitor
from LaplaceParser import LaplaceParser

class MyLaplaceVisitor(LaplaceVisitor):

    def visitLaplaceTransform(self, ctx: LaplaceParser.LaplaceTransformContext):
        # Accedemos a los términos dentro de la integral
        result = self.visit(ctx.term(0))  # Visitamos el primer término
        # Si hay más términos multiplicados, los combinamos
        for i in range(1, len(ctx.term())):
            result += " * " + self.visit(ctx.term(i))
        return result

    def visitAddExpr(self, ctx: LaplaceParser.AddExprContext):
        left = self.visit(ctx.expr())
        right = self.visit(ctx.term())
        return f"({left} + {right})"

    def visitSubExpr(self, ctx: LaplaceParser.SubExprContext):
        left = self.visit(ctx.expr())
        right = self.visit(ctx.term())
        return f"({left} - {right})"

    def visitMulExpr(self, ctx: LaplaceParser.MulExprContext):
        left = self.visit(ctx.term())
        right = self.visit(ctx.factor())
        return f"({left} * {right})"

    def visitDivExpr(self, ctx: LaplaceParser.DivExprContext):
        left = self.visit(ctx.term())
        right = self.visit(ctx.factor())
        return f"({left} / {right})"

    def visitExpFactor(self, ctx: LaplaceParser.ExpFactorContext):
        # Para e^(-s * t), la Transformada de Laplace es 1/(s+a)
        return "1/(s + a)"  # Devuelve la fórmula general para e^(-at)

    def visitFuncFactor(self, ctx: LaplaceParser.FuncFactorContext):
        # Para funciones f(t), aplicamos las reglas comunes de Transformada
        func_name = ctx.ID().getText()
        if func_name == 'f':  # Si es f(t), asumimos que es una función genérica
            return "F(s)"  # Representamos la transformada de f(t)
        return func_name

    def visitNumberFactor(self, ctx: LaplaceParser.NumberFactorContext):
        return int(ctx.NUMBER().getText())  # Retornamos el número como entero

    def visitParenExpr(self, ctx: LaplaceParser.ParenExprContext):
        return self.visit(ctx.expr())  # Visitamos la expresión dentro de los paréntesis
