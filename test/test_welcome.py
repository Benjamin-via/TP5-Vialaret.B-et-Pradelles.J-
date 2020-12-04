import bienvenue.welcome as wel

def test_hello():
    assert wel.hello('bob') == 'Hello Bob'
    assert wel.hello('Bob') == 'Hello Bob'
    assert wel.hello('') == 'Hello, my friend'
    assert wel.hello(None) == 'Hello, my friend'
    assert wel.hello('    ') == 'Hello, my friend'
    assert wel.hello('BOB') == 'HELLO BOB!'


def test_hello2():
    assert wel.hello2('Amy,Bob') == 'Hello, Amy, Bob.'
    assert wel.hello2('Amy,Bob,Joe') == 'Hello, Amy, Bob, Joe.'
    assert wel.hello2('Amy,BOB,Joe') == 'Hello, Amy, Joe. AND HELLO, BOB !'


def test_hello3():
    assert wel.hello3('Amy,Bob,Joe') == 'Hello, Amy, Bob and Joe.'
    assert wel.hello3('Amy    ,Bob,Joe') == 'Hello, Amy, Bob and Joe.'
    assert wel.hello3('Amy,Bob,!Bob,Joe') == 'Hello, Amy and Joe.'
    assert wel.hello3('Amy,Bob,!Bob,Joe,Amy') == 'Hello, Amy (x2) and Joe.'
    assert wel.hello3('Amy,Bob,!Bob,Joe,Amy,Abe,Aba,Abo,Abi') == 'Hello, world !'
    assert wel.hello3('AMY,Bob,!Bob,JOE,AMY,ABE,ABA,ABO,ABI') == 'HELLO, WORLD !'


def test_yoda():
    assert wel.yoda('bob,yoda,amy') == 'Bob, Yoda and Amy, Hello.'
    assert wel.yoda('bob,yoda,amy,Boe,Boa,Boing') == 'World, Hello'
    assert wel.yoda('bob,yodi,amy,boe,bea,beo') == 'Hello, world !'


def test_hello4():
    assert wel.hello4('Amy,*Bob*,Joe') == 'Hello, Amy, our special guest Bob, and Joe.'
    assert wel.hello4('Amy,*Bob*,*Joe*') == 'Hello, Amy, our special guest Bob, & Joe.'


def test_hello17():
    assert wel.hello17("Bob,\"Amy,Jerry") == 'Hello, Bob, and Amy,Jerry.'