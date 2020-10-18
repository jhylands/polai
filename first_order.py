class Context:
    """
    The context is the set of axoms included that permit
    the representation to be substituted.
    """
    def __init__(self):
        self.rules = []

    def add(self, statement):
        """
        The statement is presumed to
        evaluate to True
        """
        self.rules.append(statement)

class Statement:
#    def __init__(self, context):
#        self.context = context

    def __init__(self):
        print("item creation")
        self.items = []

    @property
    def a(self):
        return self.items[0]

    @a.setter
    def a(self, val):
        if self.items==[]:
            self.items = [val]
        else:
            self.items[0] == val

    @property
    def b(self):
        return self.items[1]
    @b.setter
    def b(self, val):
        if self.items == []:
            raise Exception("Can't set a b with an a")
        elif len(self.items) == 1:
            self.items.append(val)
        else:
            self.items[1] = val

    def evaluate(self):
        # type: bool
        # An empty statement is true
        return True

    def __and__(self, other):
        return And(self, other)
    def __or__(self, other):
        return Or(self, other)
    def __eq__(self, other):
        return Equivalence(self, other)

    def __nonzero__(self):
        return self.evaluate()

    # using this to mean implies backwards
    # <= as => isn't valid python
    def __le__(self, other):
        return Implies(other, self)

    def __repr__(self):
        return "Statement"

    def substitute(self, a, b):
        """
        Both a and b are considered equivalent
        Therefore where we see a, in ourselves
        we replace it with b.
        """
        if self == b:
            # replace self with b by returning b
            return b
        self.items = [i.substitute(a,b) for i in self.items]
        return self
        

class Symbol(Statement):
    def __repr__(self):
        return "Symbol"

class Constant(Symbol):
    pass

class Variables(Symbol):
    pass

class Function(Statement):

    def evaluate(self):
        # This needs to be implmented
        return False

class Predicate(Function):
    """
    A predicate is a function whose
    range is {True, False}
    """
    pass


class Connective(Predicate):
    """
    A Connective is a predicate whose
    domain is {True, False}
and or not =>
    """
    pass

class And(Connective):
    def __init__(self, a, b):
        self.items = [a, b]

    def evaluate(self):
        return bool(self.a.evaluate()) and bool(self.b.evaluate())

    def __repr__(self):
        return "({}) and ({})".format(str(self.a), str(self.b))

class Or(Connective):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def evaluate(self):
        return self.a.evaluate() or self.b.evaluate()

    def __repr__(self):
        return "({}) or ({})".format(str(self.a), str(self.b))

class Equivalence(Predicate):
    """
    A special case of Predicate
    """
    def __init__(self, a, b):
        super(Equivalence, self).__init__()
        self.a = a
        self.b = b

    def evaluate(self):
        # we need a way to have this
        # use other statements
        # `is` is strong than ==
        # but it could however be that
        # a and b are talking about the same thing
        return self.a is self.b

    def __repr__(self):
        return "({}) = ({})".format(str(self.a), str(self.b))

class Quantifier(Predicate):
    pass

class ForAll(Quantifier):
    def __init__(self, member_set, property):
        pass

class ThereExists:
    def __init__(self, member_set, property):
        pass

"""
NOTES

thing = Variable()
dog = Predicate()
ThereExists(thing, dog(thing)) => not ForAll(thing, not dog(thing))
a = Variable()
ThereExists(a, ThereExists(b, f(a,b))) == ThereExists(b, ThereExists(a, f(a,b)))
 

# Create substitution rules
f(g(x)) and f==u => u(g(x))
f(g(x)) => ThereExists(u, function(u) and u(x)==f(g(x)))
x==y => f(x)==f(y)

# So I think the top are sufficient to progress
#commutitive
comutitive(f) => f(x, y)==f(y, x)

#asociative
asociative(f) => f(a, f(b, c)) == f(f(a, b), c)

# distributive
distributive(f, g) => f(a, g(b, c)) == g(f(a, b), f(a, c))

"""
