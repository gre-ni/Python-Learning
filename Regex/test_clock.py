import pytest 
from clock_convert import convert

@pytest.mark.parametrize("time", ["9:00 AM to 5:00 PM", "9 AM to 5 PM", "9:00 AM to 5 PM", "9 AM to 5:00 PM"])
def test_valid_formats(time):
    assert convert(time) == "9:00 to 17:00"

def test_alternative_time():
    assert convert("1 PM to 11 PM") == "13:00 to 23:00"
    
def test_no_convert():
    assert convert("7:00 AM to 9:00 AM") == "7:00 to 9:00"

@pytest.mark.parametrize("wrong_format", ["5 to 6 PM", "12-14", "12 AM-2 PM", "10:66 AM to 11 PM"])
def test_wrong_format(wrong_format):
    with pytest.raises(ValueError):
        convert(wrong_format)
        
def test_midnight():
    assert convert("10 PM to 12:00 AM") == "22:00 to 00:00"