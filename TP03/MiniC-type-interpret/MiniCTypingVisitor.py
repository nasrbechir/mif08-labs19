from MiniCVisitor import MiniCVisitor
from MiniCParser import MiniCParser

from enum import Enum


class MiniCTypeError(Exception):
    pass


class BaseType(Enum):
    Float, Integer, Boolean, String = range(4)


# type functions (list of basetype -> basetype)
class FunctionType():
    def __init__(self, ret_type, arg_types):
        self.ret_type = ret_type
        self.arg_types = arg_types

    def __eq__(self, other):
        if not isinstance(other, FunctionType):
            return False
        return (self.ret_type == other.ret_type
                and (self.arg_types == other.arg_types))


# Basic Type Checking for MiniC programs.
class MiniCTypingVisitor(MiniCVisitor):

    def __init__(self):
        self._memorytypes = dict()  # id-> types
        self._current_function = None
        self._functiontypes = dict()  # id-> (FunctionType,defined)

    def _raise(self, ctx, for_what, *types):
        raise MiniCTypeError(
            'In function {}: Line {} col {}: invalid type for {}: {}'.format(
                self._current_function,
                ctx.start.line, ctx.start.column, for_what,
                ' and '.join(t.name.lower() for t in types)))

    def _raiseMismatch(self, ctx, for_what, *types):
        raise MiniCTypeError(
            'In function {}: Line {} col {}: type mismatch for {}: {}'.format(
                self._current_function,
                ctx.start.line, ctx.start.column, for_what,
                ' and '.join(t.name.lower() for t in types)))

    def _raiseNonType(self, ctx, message):
        raise MiniCTypeError(
            'In function {}: Line {} col {}: {}'.format(
                self._current_function,
                ctx.start.line, ctx.start.column, message))

    # type declaration

    def visitVarDecl(self, ctx):
        vars_l = self.visit(ctx.id_l())
        tt = self.visit(ctx.typee())
        for name in vars_l:
            if name in self._memorytypes:
                self._raiseNonType(ctx,
                                   # "Typing fun decl {}: "
                                   "Variable {1} already declared".
                                   format(self._current_function, name))
            self._memorytypes[name] = tt
        return

    def visitBasicType(self, ctx):
        if ctx.mytype.type == MiniCParser.INTTYPE:
            return BaseType.Integer
        elif ctx.mytype.type == MiniCParser.FLOATTYPE:
            return BaseType.Float
        elif ctx.mytype.type == MiniCParser.BOOLTYPE:
            return BaseType.Boolean
        elif ctx.mytype.type == MiniCParser.STRINGTYPE:
            return BaseType.String
        else:
            raise Exception("Type not implemented")

    def visitIdList(self, ctx):
        t = self.visit(ctx.id_l())
        t.append(ctx.ID().getText())
        return t

    def visitIdListBase(self, ctx):
        return [ctx.ID().getText()]

    # typing visitors for expressions, statements !

    # visitors for atoms --> value
    def visitParExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitNumberAtom(self, ctx):
        s = ctx.getText()
        try:
            int(s)
            return BaseType.Integer
        except ValueError:
            try:
                float(s)
                return BaseType.Float
            except ValueError:
                self._raiseNonType(ctx, "Invalid number atom: "+s)

    def visitBooleanAtom(self, ctx):
        return BaseType.Boolean

    def visitIdAtom(self, ctx):
        try:
            valtype = self._memorytypes[ctx.getText()]
            return valtype
        except KeyError:
            self._raiseNonType(ctx,
                               "Undefined variable {}".format(ctx.getText()))

    def visitStringAtom(self, ctx):
        return BaseType.String

    # now visit expr

    def visitAtomExpr(self, ctx):
        return self.visit(ctx.atom())

    def visitOrExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))
        if (BaseType.Boolean == lvaltype) and (BaseType.Boolean == rvaltype):
            return BaseType.Boolean
        else:
            self._raise(ctx, 'boolean operands', lvaltype, rvaltype)

    def visitAndExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))
        if (BaseType.Boolean == lvaltype) and (BaseType.Boolean == rvaltype):
            return BaseType.Boolean
        else:
            self._raise(ctx, 'boolean operands', lvaltype, rvaltype)

    def visitEqualityExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))

        if lvaltype != rvaltype:
            self._raiseMismatch(ctx, 'equality operands', lvaltype, rvaltype)

        return BaseType.Boolean

    def visitRelationalExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))

        if lvaltype != rvaltype:
            self._raise(ctx, 'relational operands', lvaltype, rvaltype)

        if lvaltype not in (BaseType.Integer, BaseType.Float):
            self._raise(ctx, 'relational operands', lvaltype, rvaltype)

        return BaseType.Boolean

    def visitAdditiveExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))

        if lvaltype != rvaltype:
            self._raise(ctx, 'additive operands', lvaltype, rvaltype)
        if lvaltype not in (BaseType.Integer, BaseType.Float, BaseType.String):
            self._raise(ctx, 'additive operands', lvaltype, rvaltype)
        if ctx.myop.type != MiniCParser.PLUS and lvaltype == BaseType.String:
            self._raise(ctx, 'additive operands', lvaltype, rvaltype)

        return lvaltype

    def visitMultiplicativeExpr(self, ctx):
        lvaltype = self.visit(ctx.expr(0))
        rvaltype = self.visit(ctx.expr(1))

        if lvaltype != rvaltype:
            self._raise(ctx, 'multiplicative operands', lvaltype, rvaltype)

        if lvaltype not in (BaseType.Integer, BaseType.Float):
            self._raise(ctx, 'multiplicative operands', lvaltype, rvaltype)

        return lvaltype

    def visitNotExpr(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.Boolean:
            self._raise(ctx, 'not expression', etype)
        else:
            return BaseType.Boolean

    def visitUnaryMinusExpr(self, ctx):
        etype = self.visit(ctx.expr())
        if etype not in (BaseType.Integer, BaseType.Float):
            self._raise(ctx, 'unary minus operand', etype)

        return etype

    # Typing functions
    def visitParamDecl(self, ctx):
        name = ctx.ID().getText()
        tt = self.visit(ctx.typee())
        if name in self._memorytypes:
            raise self._raiseNonType(ctx,
                                     "Parameter {} already defined".format(name))
        else:
            self._memorytypes[name] = tt
        return tt

    def visitExprListEmpty(self, ctx):
        return []

    def visitExprListNonEmpty(self, ctx):
        return self.visit(ctx.expr_l_nonempty())

    def visitParamListEmpty(self, ctx):
        return []

    def visitParamListNonEmpty(self, ctx):
        return self.visit(ctx.param_l_nonempty())

    def visitParamListBase(self, ctx: MiniCParser.ExprListContext):
        return [self.visitChildren(ctx)]

    def visitExprListBase(self, ctx: MiniCParser.ExprListContext):
        return [self.visitChildren(ctx)]

    def visitExprList(self, ctx):
        exprTypeList = [self.visit(ctx.expr())]
        exprTypeList += (self.visit(ctx.expr_l()))
        return exprTypeList

    def visitParamList(self, ctx):
        paramTypeList = [self.visit(ctx.param())]
        paramTypeList += (self.visit(ctx.param_l()))
        return paramTypeList

    def visitFuncDecl(self, ctx):
        funcname = ctx.ID().getText()
        self._current_function = funcname
        self._memoryType = dict()
        returnType = self.visit(ctx.typee())
        paramTypes = self.visit(ctx.param_l())
        if funcname in self._functiontypes:
            if (FunctionType(returnType, paramTypes)
                    != self._functiontypes[funcname][0]):
                raise self._raiseNonType(
                    ctx, "function {} already declared with a different signature"
                    .format(funcname))
            if self._functiontypes[funcname][1]:
                raise self._raiseNonType(
                    ctx, "function {} already defined".format(funcname))
        self._functiontypes[funcname] = (FunctionType(returnType, paramTypes), True)
        self.visit(ctx.vardecl_l())
        if False:
            print("current environnement when typing the body of "
                  + funcname+":"+str(paramTypes)+"->"+str(returnType))
            print(self._memorytypes)  # debug typing env
        self.visit(ctx.block())
        tt = self.visit(ctx.expr())
        if tt != returnType:
            self._raiseMismatch(ctx, "return type of function " + funcname, returnType, tt)
        # here store the type of the function.
        self._memorytypes = dict()
        self._current_function = None
        return

    def visitFuncDeclEmpty(self, ctx):
        funcname = ctx.ID().getText()
        self._current_function = funcname
        returnType = self.visit(ctx.typee())
        paramTypes = self.visit(ctx.param_l())
        if funcname in self._functiontypes:
            if (FunctionType(returnType, paramTypes)
                    != self._functiontypes[funcname][0]):
                raise self._raiseNonType(
                    ctx, "function {} already declared with a different signature"
                    .format(funcname))
        else:
            self._functiontypes[funcname] = (FunctionType(returnType, paramTypes), False)
        if False:
            print(str(FunctionType(returnType, paramTypes).arg_types))
        self._memorytypes = dict()
        self._current_function = None

    def visitFuncCall(self, ctx):
        funcname = ctx.ID().getText()
        expr_types = self.visit(ctx.expr_l())
        try:
            functype = self._functiontypes[funcname][0]
        except KeyError:
            self._raiseNonType(ctx, "Undefined function {}".format(funcname))
        par_types = functype.arg_types
        if len(par_types) != len(expr_types):
            self._raiseNonType(ctx,
                               "wrong number of arguments in call to function "+funcname)
        for i in range(len(par_types)):
            if expr_types[i] != par_types[i]:
                self._raiseMismatch(ctx, "method argument in call to function " +
                                    funcname, expr_types[i], par_types[i])
        return functype.ret_type

    # visit statements

    def visitPrintintStat(self, ctx):
        etype = self.visit(ctx.expr())
        if etype not in (BaseType.Integer, BaseType.Boolean):
            self._raise(ctx, 'println_int statement', etype)

    def visitPrintfloatStat(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.Float:
            self._raise(ctx, 'println_float statement', etype)

    def visitPrintstringStat(self, ctx):
        etype = self.visit(ctx.expr())
        if etype != BaseType.String:
            self._raise(ctx, 'println_string statement', etype)

    def visitAssignStat(self, ctx):
        valtype = self.visit(ctx.expr())
        name = ctx.ID().getText()
        if name not in self._memorytypes:
            self._raiseNonType(  # "Typing function " + self._current_function + ": "
                ctx, "Undefined variable "+name)
        if self._memorytypes[name] != valtype:
            self._raiseMismatch(  # "Typing function " + self._current_function + ": "
                ctx, name, self._memorytypes[name], valtype)

    def visitCondBlock(self, ctx):
        condtype = self.visit(ctx.expr())
        if condtype != BaseType.Boolean:
            self._raise(ctx, 'conditional block', condtype)
        self.visit(ctx.stat_block())

    def visitWhileStat(self, ctx):
        condtype = self.visit(ctx.expr())
        if condtype != BaseType.Boolean:
            self._raise(ctx, 'while condition', condtype)
        self.visit(ctx.stat_block())

    def visitIfStat(self, ctx):
        for cond in ctx.condition_block():
            self.visit(cond)
        if ctx.stat_block() is not None:
            self.visit(ctx.stat_block())
