import pytest
from validation import validate_filename

def test_valid_filename():
    assert validate_filename("report_2025.txt") == "report_2025.txt"

def test_invalid_filename():
    with pytest.raises(ValueError):
        validate_filename("bad/../file.txt")