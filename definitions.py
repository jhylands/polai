class Function:
    def __init__(self):
        self.commutitive
        self.asociative

    def __call__(self, expression):
        pass

class Primitive:
    """
    These are things which are axiomatically
    existant objects
    """
    def __init__(self, name):
        self.name = name

class Abstraction:
    def __init__(self):
        pass

class Term:
    def __init__(self):
        self.tree
    
class Expression:
    def __init__(self):
        self.terms = []

    def __iter__(self):
        return iter(self.terms)

class Equation:
    def __init__(self, lhs, rhs):
        # type: (Equation, Expression, Expression)->None
        self.lhs = lhs
        self.rhs = rhs

    def apply(self, f):
        # Maybe we need to work out how best to define f
        self.lhs = f(self.lhs)
        self.rhs = f(self.rhs)


