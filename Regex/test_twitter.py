import pytest
from twitter import extract_username_a, extract_username_b

test_inputs = ["twitter.com/niki", "http://twitter.com/niki", "https://twitter.com/niki", "www.twitter.com/niki", "https://www.twitter.com/niki"]

@pytest.mark.parametrize("url", test_inputs)
def test_version_a(url):
    assert extract_username_a(url) == "niki"
    
@pytest.mark.parametrize("url", test_inputs)
def test_version_b(url):
    assert extract_username_b(url) == "niki"
    
def test_wrong_url():
    assert extract_username_b("google.com/niki") == None

def test_no_username():
    assert extract_username_b("www.twitter.com") == None