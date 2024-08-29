from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("hola") == 20
    assert value("Halo") == 20

def test_other():
    assert value("What's up") == 100