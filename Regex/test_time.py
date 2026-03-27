import pytest
from time_elapsed import get_date, parse_date_format

# Tuple for testing:
date_future = (2055,2,31)
date_invalid = (2000,2,31)


@pytest.mark.parametrize("invalid_format", ["cat", "17 January, 1999", "1999-3-4", "26-08-08", "1992/04/03"])
def test_invalid_format(invalid_format):
    with pytest.raises(ValueError):
        parse_date_format(invalid_format)

@pytest.mark.parametrize("invalid_format", ["1999-20-03", "1999-00-05"])
def test_invalid_month(invalid_format):
    with pytest.raises(ValueError):
        parse_date_format(invalid_format)

def test_date_future():
    with pytest.raises(ValueError):
        get_date(date_future)

def test_invalid_date():
    with pytest.raises(ValueError):
        get_date(date_invalid)

def test_date_conversion():
    assert parse_date_format("1999-02-04") == (1999,2,4)
