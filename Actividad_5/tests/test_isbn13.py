import pytest
from src import isbn


@pytest.mark.parametrize("s", [
    "9780306406157",
    "978-3-16-148410-0",
])
def test_isbn13_valid(s):
    assert isbn.is_valid_isbn13(s)


@pytest.mark.parametrize("s", [
    "978030640615",     # longitud 12
    "97803064061570",   # longitud 14
    "978030640615A",    # char ilegal
    "9780306406158",    # checksum wrong
])
def test_isbn13_invalid(s):
    assert not isbn.is_valid_isbn13(s)


def test_detect_isbn13():
    assert isbn.detect_isbn("978-3-16-148410-0") == 'ISBN-13'
    assert isbn.detect_isbn("") == 'INVALID'