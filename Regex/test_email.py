from email_validation import validate_email
import pytest


supported_domains = [".edu",".com",".cz",".eu"]

# Missing values:
def test_missing_at():
    assert not validate_email("haha.edu")

def test_missing_domain():
    assert not validate_email("haha@haha")

def test_multiple_ats():
    assert not validate_email("haha@@haha.com")

def test_special_char():
    assert not validate_email("&haha@haha.com")

def test_multiple_dots():
    assert not validate_email("hah..ha@haha.com")
    

# Happy paths:
@pytest.mark.parametrize("domain", supported_domains)
def test_supported_domains(domain):
    assert validate_email(f"test@test{domain}")

@pytest.mark.parametrize("dot_email", ["hah.hah@haha.com", "haha@hh.ha.com", "ha.ha@ha.ha.com"])
def test_email_with_dot(dot_email):
    assert validate_email(dot_email)

def test_all_uppercase():
    assert validate_email("HAHA@HAHA.COM")

