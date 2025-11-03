# Plan de pruebas — ISBN Validator

## Objetivo
Diseñar y ejecutar pruebas unitarias para asegurar la correcta normalización y validación de ISBN-10 y ISBN-13.

## Alcance
Funciones: normalize_isbn, is_valid_isbn10, is_valid_isbn13, detect_isbn.

## Supuestos
- Entradas nulas/ vacías se tratan como inválidas.
- Separadores aceptados: espacios y guiones.

## Particiones de equivalencia
- ISBN-10:
  - Válidos (dígitos)
  - Válidos (con 'X' al final)
  - Inválidos (checksum)
  - Inválidos (longitud ≠10)
  - Inválidos (caracteres no permitidos)
- ISBN-13:
  - Válidos (13 dígitos)
  - Inválidos (checksum)
  - Inválidos (longitud)
  - Inválidos (caracteres no dígitos)

## Análisis de fronteras
- Longitudes probadas: 9, 10, 11 (ISBN-10) y 12, 13, 14 (ISBN-13).
- Cadena vacía y entrada nula.

## Métricas objetivo
- Cobertura líneas ≥ 90%
- Cobertura branches ≥ 85%

## Riesgos
- Tests dependientes de implementación (caja blanca) pueden cambiar si se refactoriza.
- Uso de librerías externas en CI podría romper reproducibilidad.
