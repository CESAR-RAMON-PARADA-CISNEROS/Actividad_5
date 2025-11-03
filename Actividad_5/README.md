# Validador de ISBN — Actividad 5

En este repositorio: Se guarda la implementación y pruebas para un validador de ISBN (ISBN-10 e ISBN-13).

## Cómo se ejecuta localmente

```bash
python -m venv .venv
.venv\Scripts\activate     # Para Windows
pip install -U pip
pip install pytest coverage
coverage run -m pytest
coverage html -d coverage_html
open coverage_html/index.html
```

## Estructura de las carpetas
src/, tests/, .github/workflows/

## Decisiones y supuestos
- No se utiliza ninguna biblioteca ISBN externa.
- normalize_isbn devuelve mayúsculas y elimina solo espacios/guiones.
- Solo se permite «X» como última letra mayúscula en ISBN-10.