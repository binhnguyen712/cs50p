from seasons import validate
import pytest
from datetime import date
import sys
def test_incorrect_format():
    with pytest.raises(SystemExit):
        validate("January 1, 2020") == sys.exit()
        validate("1991-02-35") == sys.exit()

def test_correct_date():
    assert validate("1999-01-01") == date(1999,1,1)
