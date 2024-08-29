from numb3rs import validate

def test_valid():
    assert validate("123.1.34.12") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_firstbyte():
    assert validate("345.12.34.255") == False

def test_otherbyte():
    assert validate("255.345.0.253") == False
    assert validate("254.123.256.123") == False

def test_notdigit():
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
    assert validate("cat") == False