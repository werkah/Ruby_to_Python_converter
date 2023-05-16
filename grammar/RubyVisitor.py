# Generated from C:\Users\wehil\PycharmProjects\Ruby-to-Python-converter\grammar\Ruby.g4 by ANTLR 4.12.0
from antlr4 import *
from grammar.RubyParser import RubyParser


# This class defines a complete generic visitor for a parse tree produced by RubyParser.

class RubyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RubyParser#program.
    def visitProgram(self, ctx: RubyParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#statementList.
    def visitStatementList(self, ctx: RubyParser.StatementListContext):
        print("StatementList")
        result = []
        for child in ctx.getChildren():
            if isinstance(child, TerminalNode):
                continue
            statement = self.visit(child)
            # print("STATEMENT",statement)
            if statement:
                result.append(statement)
        # print("ReSULT",''.join(result))
        return ''.join(result)

    # Visit a parse tree produced by RubyParser#terminator.
    def visitTerminator(self, ctx:RubyParser.TerminatorContext): ###TUTAJ ZMIENIŁAM
        if ctx.SEMICOLON():
            return "\n"
        elif ctx.NEWLINE():
            return "\n"

    # Visit a parse tree produced by RubyParser#statement.
    def visitStatement(self, ctx: RubyParser.StatementContext):
        print("Statement")
        if ctx.functions():
            return self.visitFunctions(ctx.functions())
        elif ctx.instructions():
            return self.visitInstructions(ctx.instructions())
        elif ctx.loop():
            return self.visitLoop(ctx.loop())
        elif ctx.variables():
            return self.visitVariables(ctx.variables())
        elif ctx.assignment():
            return self.visitAssignment(ctx.assignment())
        elif ctx.classObject():
            return self.visitClassObject(ctx.classObject())
        elif ctx.methodCall():
            return self.visitMethodCall(ctx.methodCall())
        elif ctx.COMMENT():
            return f"{ctx.getText()}"
        elif ctx.putsFunction():
            return self.visitPutsFunction(ctx.putsFunction())
        elif ctx.class_():
            return self.visitClass_(ctx.class_())
        else:
            raise NotImplementedError(f"Not implemented: {ctx.getText()}")

    # Visit a parse tree produced by RubyParser#functions.
    def visitFunctions(self, ctx: RubyParser.FunctionsContext):
        print("Functions")
        if ctx.function():
            return self.visit(ctx.function())
        else:
            return self.visit(ctx.functionCall())

    # Visit a parse tree produced by RubyParser#instructions.
    def visitInstructions(self, ctx: RubyParser.InstructionsContext):
        print("Instructions")
        if ctx.ifInstruction():
            return self.visit(ctx.ifInstruction())
        else:
            return self.visit(ctx.unlessInstruction())

    # Visit a parse tree produced by RubyParser#loop.
    def visitLoop(self, ctx: RubyParser.LoopContext):
        print("Loop")
        if ctx.whileLoop():
            return self.visit(ctx.whileLoop())
        elif ctx.forLoop():
            return self.visit(ctx.forLoop())
        else:
            return self.visit(ctx.untilLoop())

    # Visit a parse tree produced by RubyParser#bool.
    def visitBool(self, ctx: RubyParser.BoolContext):
        print("Bool")
        return ctx.getText()[0].upper() + ctx.getText()[1:]

    # Visit a parse tree produced by RubyParser#type.
    def visitType(self, ctx: RubyParser.TypeContext):
        print("Type")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#array.
    def visitArray(self, ctx: RubyParser.ArrayContext):
        result = ""
        for child in ctx.getChildren():
            if child.getChildCount() == 0:
                res = child.getText()
                result += res
            else:
                result += str(self.visit(child))
        return result

    # Visit a parse tree produced by RubyParser#value.
    def visitValue(self, ctx: RubyParser.ValueContext):
        if ctx.NUMBER():
            return float(ctx.NUMBER().getText()) if '.' in ctx.NUMBER().getText() else int(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()
        else:
            return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#ifInstruction.
    def visitIfInstruction(self, ctx: RubyParser.IfInstructionContext): ####TUTAJ ZMIANA
        print("IfInstruction")
        result = ""
        # print(ctx.getText())
        # print(ctx.getChildCount())
        i=0
        # for child in ctx.getChildren():
        #     print(i,child.getText())
        #     i+=1
        # print(self.visitCondition(ctx.condition()))
        for i in range(0,ctx.getChildCount()):
            if ctx.getChild(i) ==ctx.IF():
                result += str(ctx.getChild(i).getText())
            elif ctx.getChild(i) == ctx.condition():
                # self.visitCondition(ctx.condition())
                print("CONDITION")
                result += self.visit(ctx.condition())
            elif ctx.getChild(i) == ctx.ELSE():
                result += str(ctx.getChild(i).getText())
            elif ctx.getChild(i) == ctx.ELSIF():
                result += str(ctx.getChild(i).getText())
            elif ctx.getChild(i) == ctx.END():
                result += str(ctx.getChild(i).getText())
            elif ctx.getChild(i) == ctx.crlf():
                print("CRLF")
                result+= self.visit(ctx.crlf()) ####tu problem z terminatorem

        return result

    # Visit a parse tree produced by RubyParser#unlessInstruction.
    def visitUnlessInstruction(self, ctx: RubyParser.UnlessInstructionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#whileLoop.
    def visitWhileLoop(self, ctx: RubyParser.WhileLoopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#forLoop.
    def visitForLoop(self, ctx: RubyParser.ForLoopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#untilLoop.
    def visitUntilLoop(self, ctx: RubyParser.UntilLoopContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#comparisonOperator.
    def visitComparisonOperator(self, ctx: RubyParser.ComparisonOperatorContext):   ####TUTAJ ZMIANA
        operator=ctx.getText()
        if operator == '==':
            return '=='
        elif operator == '!=':
            return '!='
        elif operator == '>':
            return '>'
        elif operator == '>=':
            return '>='
        elif operator == '<':
            return '<'
        elif operator == '<=':
            return '<='
        elif operator == '<=>':
            return '<=>'
        elif operator == '===':
            return '==='

    # Visit a parse tree produced by RubyParser#operator.
    def visitOperator(self, ctx: RubyParser.OperatorContext):
        operator = ctx.getText()
        if operator == '+':
            return '+'
        elif operator == '-':
            return '-'
        elif operator == '*':
            return '*'
        elif operator == '/':
            return '/'
        elif operator == '%':
            return '%'
        elif operator == '**':
            return '**'
        elif operator == '++':
            return '++'
        elif operator == '--':
            return '--'

    # Visit a parse tree produced by RubyParser#condition.
    def visitCondition(self, ctx: RubyParser.ConditionContext): ####TUTAJ ZMIANA
        print("Condition")
        result = ""
        print(ctx.getText())
        print(ctx.getChildCount())
        for i in range(0, ctx.getChildCount()):
            print(i, ctx.getChild(i).getText())
        for i in range(0, ctx.getChildCount()):
            if ctx.getChild(i) == ctx.comparisonOperator():
                result += str(self.visit(ctx.comparisonOperator()))
            elif ctx.getChild(i) == ctx.value():
                result += str(self.visit(ctx.value()))
            elif ctx.getChild(i) == ctx.ID():
                result += str(self.visit(ctx.ID()))
        print("Result- condition", result)
        return result

    # Visit a parse tree produced by RubyParser#variables.
    def visitVariables(self, ctx: RubyParser.VariablesContext):
        print("Variables")
        var_value = self.visit(ctx.getChild(2))
        return f"{ctx.ID()[0].getText()} = {var_value}"

    # Visit a parse tree produced by RubyParser#sign.
    def visitSign(self, ctx: RubyParser.SignContext):
        if ctx.PLUS():
            return '+'
        else:
            return '-'

    # Visit a parse tree produced by RubyParser#mathOperation.
    def visitMathOperation(self, ctx):
        print("Mathoperation")
        result = ""
        if ctx.sign():
            result += str(self.visitSign(ctx.sign()))
        result += str(self.visit(ctx.getChild(0)))
        for i in range(1, ctx.getChildCount()):
            # print("CHILD", ctx.getChild(i))
            child = ctx.getChild(i)
            if child.getChildCount() == 0:
                res = child.getText()
                result += res
            else:
                result += str(self.visit(child))
            # print("RESULT", result)
        return result

    # Visit a parse tree produced by RubyParser#bracketExpression.
    def visitBracketExpression(self, ctx):
        return "(" + self.visit(ctx.mathOperation()) + ")"

    # Visit a parse tree produced by RubyParser#function.
    def visitFunction(self, ctx: RubyParser.FunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#parameters.
    def visitParameters(self, ctx: RubyParser.ParametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#class.
    def visitClass_(self, ctx: RubyParser.ClassContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#classBody.
    def visitClassBody(self, ctx: RubyParser.ClassBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#functionCall.
    def visitFunctionCall(self, ctx: RubyParser.FunctionCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx: RubyParser.AssignmentOperatorContext):
        operator = ctx.getText()
        if operator == '+=':
            return '+='
        elif operator == '-=':
            return '-='
        elif operator == '*=':
            return '*='
        elif operator == '**=':
            return '**='
        elif operator == '/=':
            return '%'
        elif operator == '%=':
            return '%='

    # Visit a parse tree produced by RubyParser#loopBody.
    def visitLoopBody(self, ctx: RubyParser.LoopBodyContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#assignment.
    def visitAssignment(self, ctx: RubyParser.AssignmentContext): ####TUTAJ ZMIANA
        result = ""
        # print("Assignment")
        # print(ctx.getText())
        # print(ctx.getChildCount())
        for i in range(0, ctx.getChildCount()):
            if i == 0:
                result+= ctx.ID()[0].getText()
            else:
                result+= str(self.visit(ctx.getChild(i)))
            # print("RESULT", result)

        return result


    # Visit a parse tree produced by RubyParser#classObject.
    def visitClassObject(self, ctx: RubyParser.ClassObjectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#methodCall.
    def visitMethodCall(self, ctx: RubyParser.MethodCallContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RubyParser#putsFunction.
    def visitPutsFunction(self, ctx: RubyParser.PutsFunctionContext):   ###Zmiana, ale nie wszytskie wartosci
        # value = self.visit(ctx.getChild(2))                           ###nie ma functionCall i objectCall
        # print("PutsFunction")
        # print(value)
        # print(ctx.getText())
        result = ""
        for i in range(0, ctx.getChildCount()):
            if ctx.getChild(i)==ctx.ID():
                result+= str(ctx.ID().getText())
            elif ctx.getChild(i) == ctx.value():
                result+= str(self.visit(ctx.value()))
            elif ctx.getChild(i)==ctx.array():
                result+= str(self.visit(ctx.array()))
        return f"print({result})"

    # Visit a parse tree produced by RubyParser#crlf.
    def visitCrlf(self, ctx: RubyParser.CrlfContext):
        return "\n"


del RubyParser
