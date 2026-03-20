import pytest
from ip_format_check import validate_ip_address

@pytest.mark.parametrize("address", ["1.2.3.4", "127.0.0.1", "255.255.255.255"])
def test_valid_address(address):
    assert(address)

@pytest.mark.parametrize("address", ["275.3.6.1", "512.512.512.512"])
def test_too_high(address):
    assert not validate_ip_address(address)

@pytest.mark.parametrize("address", ["3.3.4","1.2.3.1000"])
def test_wrong_digitnum(address):
    assert not validate_ip_address(address)

def test_extra_zero():
    assert not validate_ip_address("192.168.001.1")

def test_non_numeric():
    assert not validate_ip_address("cat")