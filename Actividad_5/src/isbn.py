"""
Funciones para normalizar y validar ISBN-10 e ISBN-13.
No usa librerías externas y no tiene efectos secundarios al importarse.
"""
from typing import Optional


def normalize_isbn(s: Optional[str]) -> str:
    """Eliminar espacios y guiones; devolver cadena vacía si entrada nula o vacía.
    Convierte a mayúsculas para manejar 'x' -> 'X'.
    """
    if s is None:
        return ""
    s = s.strip()
    if not s:
        return ""
    # Quitar espacios, tabs, guiones y NBSP
    cleaned = ''.join(ch for ch in s if ch not in (' ', '\t', '-', '\u00A0'))
    # Uppercase para 'x' -> 'X'
    cleaned = cleaned.upper()
    return cleaned


def is_valid_isbn10(s: Optional[str]) -> bool:
    """Valida ISBN-10:
    - Normaliza la cadena
    - Debe tener longitud 10
    - Los primeros 9 chars deben ser dígitos
    - El último puede ser dígito o 'X' (que representa 10)
    - Suma ponderada con weights 10..1; válido si total % 11 == 0
    """
    s = normalize_isbn(s)
    if len(s) != 10:
        return False
    if not all(ch.isdigit() for ch in s[:9]):
        return False
    last = s[9]
    if not (last.isdigit() or last == 'X'):
        return False

    total = 0
    for i in range(10):
        ch = s[i]
        weight = 10 - i
        value = 10 if ch == 'X' else (ord(ch) - ord('0'))
        total += weight * value
    return total % 11 == 0


def is_valid_isbn13(s: Optional[str]) -> bool:
    """Valida ISBN-13:
    - Normaliza la cadena
    - Debe tener longitud 13 y todos dígitos
    - Pesos alternos 1 y 3; válido si total % 10 == 0
    """
    s = normalize_isbn(s)
    if len(s) != 13:
        return False
    if not s.isdigit():
        return False

    total = 0
    for i, ch in enumerate(s):
        value = ord(ch) - ord('0')
        weight = 1 if i % 2 == 0 else 3
        total += weight * value
    return total % 10 == 0


def detect_isbn(s: Optional[str]) -> str:
    """Normaliza y detecta: devuelve 'ISBN-10', 'ISBN-13' o 'INVALID'."""
    clean = normalize_isbn(s)
    if not clean:
        return 'INVALID'
    if len(clean) == 10 and is_valid_isbn10(clean):
        return 'ISBN-10'
    if len(clean) == 13 and is_valid_isbn13(clean):
        return 'ISBN-13'
    return 'INVALID'
