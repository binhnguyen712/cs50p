from plates import is_valid

def test_punctuation():
    assert is_valid("AA?22") == False
    assert is_valid("PI3.14") == False

def test_number():
    assert is_valid("0BC") == False
    assert is_valid("356384") == False

def test_valid():
    assert is_valid("AAA222") == True
    assert is_valid("HELLO") == True

def test_notinmiddle():
    assert is_valid("AB0A34") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    assert is_valid("A91283") == False
    assert is_valid("AAA22A") == False

def test_length():
    assert is_valid("ABC") == True
    assert is_valid("Hello123") == False
    assert is_valid("FG") == True
    assert is_valid("D") == False
    assert is_valid("A0") == False