import random
from src import isbn


def random_isbn10_like():
    """Genera un ISBN-10 válido aleatorio (sin separadores)."""
    digits = [random.randint(0, 9) for _ in range(9)]
    total = sum((10 - i) * d for i, d in enumerate(digits))
    check = (-total) % 11
    last = 'X' if check == 10 else str(check)
    return ''.join(str(d) for d in digits) + last


def test_normalize_idempotent_random():
    for _ in range(50):
        s = random.choice([
            random_isbn10_like(),
            "978-3-16-148410-0",
            "0 306 40615 2",
            None,
            ""
        ])
        assert isbn.normalize_isbn(isbn.normalize_isbn(s)) == isbn.normalize_isbn(s)


def test_format_invariance_examples():
    base = "9780306406157"
    variants = ["978-0-306-40615-7", "978 0306406157", " 9780306406157 "]
    for v in variants:
        assert isbn.normalize_isbn(v) == isbn.normalize_isbn(base)
        assert isbn.detect_isbn(v) == 'ISBN-13'
