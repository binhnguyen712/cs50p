from um import count

def test_case_insensitive():
    assert count("hello, um, world, UM?") == 2

def test_incorrect_use():
    assert count("hello yummy, um, world") == 1

def test_correct_use():
    assert count("hello, um, world") == 1
