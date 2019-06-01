from asserts import *

class Symbol(str):
    pass

class Environment(dict):
    class GlobalBuiltIns(dict):
        exec(open("./built_ins.py").read())

    def __init__(self):
        self.parents = []

    def __setitem__(self, symbol, value):
        super().__setitem__(symbol, value)

    def __delitem__(self, symbol, value):
        super().__delitem__(symbol)

    def __getitem__(self, symbol):
        try:
            return super().__getitem__(symbol)
        except KeyError:
            if self.parents:
                for parent in self.parents:
                    try:
                        return parent.lookup_symbol(symbol)
                    except KeyError:
                        pass
            else:
                if symbol in Environment.GlobalBuiltIns.built_ins:
                    return Environment.GlobalBuiltIns.built_ins[symbol]
        raise KeyError(f"The symbol {symbol} is not defined")

def eval_expr(obj, env):
    if type(obj) is list:
        if not obj:
            return obj
        operator = eval_expr(obj[0], env)
        return operator(env, *obj[1:])

    if isinstance(obj, Symbol):
        return env[obj]

    if callable(obj)    or \
       type(obj) is str or \
       type(obj) is int or \
       type(obj) is float:
        return obj


def eval_params(env, params):
    return [eval_expr(p, env) for p in params]

def p1(env, number):
    return number + 1

env = Environment()

env["+1"] = p1
env["pi"] = 3.14159256359878

print(eval_expr([Symbol("+"), 1, 2, eval_expr([Symbol("+"), 1, 2, 3], env)], env))
print(eval_expr([Symbol("-"), 1, 2, 3], env))
print(eval_expr([Symbol("-"), 3], env))
print(eval_expr([Symbol("+1"), 3], env))
print(eval_expr(Symbol("pi"), env))
