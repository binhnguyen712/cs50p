from twttr import shorten

def test_case_sensitivity():
    assert shorten("FACEBOOK") == "FCBK"
    assert shorten("instagram") == "nstgrm"

def test_no_vowels():
    assert shorten("myth") == "myth"

def test_include_numbers():
    assert shorten("YouTube123") == "YTb123"

def test_include_punctuation():
    assert shorten("Google:'") == "Ggl:'"

