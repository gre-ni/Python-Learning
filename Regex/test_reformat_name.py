import pytest
from format_input import reformat_name

@pytest.mark.parametrize("formats", ["Good, Jane", "Good,Jane"])
def test_input(formats):
    assert reformat_name(formats) == "Jane Good"