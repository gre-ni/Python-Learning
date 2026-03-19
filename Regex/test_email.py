from email_validation import validate_email
import pytest


supported_domains = [".edu",".com",".cz",".edu"]

# Missing values:
def test_missing_at():
    assert validate_email("haha.edu") == False

def test_missing_domain():
    assert validate_email("haha@haha") == False

def test_multiple_ats():
    assert validate_email("haha@@haha.com") == False

def test_special_char():
    assert validate_email("&haha@haha.com") == False

def test_multiple_dots():
    assert validate_email("hah..ha@haha.com") == False

@pytest.mark.parametrize("short_email", ["h@haha.com", "haha@h.com"])
def test_too_short(short_email):
    assert validate_email(short_email) == False

# Happy paths:
@pytest.mark.parametrize("domain", supported_domains)
def test_supported_domains(domain):
    assert validate_email(f"test@test{domain}") == True

def email_with_dot():
    assert validate_email("haha.hah@gmail.com") == True

