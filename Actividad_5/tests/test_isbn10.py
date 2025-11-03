import pytest
from src import isbn


@pytest.mark.parametrize("s", [
    "0-306-40615-2",
    "0471958697",
    "0306406152",
    "0-8044-2957-X",
    "080442957X",
])
def test_isbn10_valid(s):
    assert isbn.is_valid_isbn10(s)


@pytest.mark.parametrize("s", [
    "123456789",       # longitud 9
    "12345678901",     # longitud 11
    "0-8044-2957-A",   # char ilegal
    "0306406153",      # checksum incorrecto
    "0-8044-295-X7",   # 'X' no en última posición
])
def test_isbn10_invalid(s):
    assert not isbn.is_valid_isbn10(s)


def test_normalize_handles_lower_x():
    assert isbn.normalize_isbn("0-8044-2957-x") == "080442957X"
    assert isbn.is_valid_isbn10("0-8044-2957-x")  # debe ser válido tras normalize


def test_detect_isbn10():
    assert isbn.detect_isbn("0-306-40615-2") == 'ISBN-10'
