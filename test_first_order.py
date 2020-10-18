from first_order import *

def test_statement():
    assert Statement().evaluate()

def test_equality():
    thing = Constant()
    assert Equivalence(thing, thing).evaluate()
    assert (thing==thing).evaluate()

def test_inequality():
    a = Constant()
    b = Constant()
    assert not Equivalence(a, b).evaluate()
    assert not (a==b).evaluate()


def test_and():
    thing = Constant()
    assert (Equivalence(thing, thing) and Equivalence(thing, thing)).evaluate()

def test_nand():
    thing = Constant()
    a = Constant()
    b = Constant()
    result = (thing==thing and a==b).evaluate()
    assert not result

def test_or():
    thing = Constant()
    a = Constant()
    b = Constant()
    result = (thing==thing or a==b).evaluate()
    assert result
    
def test_nor():
    a = Constant()
    b = Constant()
    result = (a==b or a==b).evaluate()
    assert not result

def test_substitute():
    a = Constant()
    b = Constant()
    statement = (a==b).substitute(b,a)
    print(statement)
    assert statement.evaluate()

    statement = (a==b and a==b).substitute(b,a)
    print(statement)
    assert statement.evaluate()
    


