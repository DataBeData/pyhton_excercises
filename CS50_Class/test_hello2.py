from hello2 import hello

'''def test_hello():
    hello("David") == "hello, David"'''

def test_default():
    assert hello() == "hello, world"

def test_argument():
    for name in ["Jo","Dave","Ruben"]:
        assert hello() == f"hello, {name}"
        