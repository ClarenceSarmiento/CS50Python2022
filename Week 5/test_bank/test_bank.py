from bank import value

def test_hello():
    assert(value("Hello")) == 0
    assert(value("hello, world")) == 0
    assert(value("HELLO WORLD!")) == 0

def test_h():
    assert(value("Hi")) == 20
    assert(value("hi, world")) == 20
    assert(value("HI, WORLD!")) == 20

def test_random():
    assert(value("yow!")) == 100
    assert(value("Wazzup!")) == 100