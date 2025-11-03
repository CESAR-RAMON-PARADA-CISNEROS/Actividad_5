# Reporte Técnico — ISBN Validator

## 1. Resumen
Este proyecto implementa y prueba un validador de ISBN (ISBN-10 e ISBN-13). Se incluyen: implementación del módulo, suite de pruebas unitarias, propiedades básicas y un workflow de CI que genera reporte de cobertura.

## 2. Implementación
Las funciones principales son:
- `normalize_isbn(s)`: elimina espacios y guiones, convierte a mayúsculas.
- `is_valid_isbn10(s)`: valida según peso 10..1 y permite 'X' al final.
- `is_valid_isbn13(s)`: valida según pesos 1/3 alternos.
- `detect_isbn(s)`: retorna 'ISBN-10', 'ISBN-13' o 'INVALID'.

**Decisiones de diseño**
- No se usaron librerías externas; el módulo es determinista y sin efectos secundarios.
- 'X' se normaliza a mayúscula y sólo se acepta en la última posición del ISBN-10.

## 3. Uso de IA
**IA usada:** Se utilizó ChatGPT como apoyo para generar estructuras de código, ejemplos de tests y plantillas de workflow. La IA se empleó únicamente como asistente. Todas las piezas de código entregadas fueron revisadas, adaptadas y validadas manualmente por el autor del repositorio. Las pruebas se ejecutaron localmente y en CI; se añadieron casos extra para cubrir rutas de error y fronteras.

## 4. Plan de pruebas y trazabilidad
El plan de pruebas se diseñó para cubrir las funciones principales del módulo. Se definieron particiones de equivalencia y análisis de fronteras para asegurar una cobertura amplia. Vease el arhivo [plan_pruebas.md](plan_pruebas.md) para detalles completos.

## 5. Resultados
Durante la ejecución de la suite de pruebas con pytest y coverage.py, se obtuvieron resultados exitosos en todas las pruebas implementadas.
El total de 18 pruebas se ejecutó correctamente, sin fallos ni errores.
La cobertura alcanzada fue del 99 % en líneas y 98 % en ramas, superando ampliamente los objetivos establecidos en el plan de pruebas (≥ 90 % líneas y ≥ 85 % ramas).

Estos valores demuestran que la suite de pruebas cubre prácticamente todas las rutas lógicas del código, incluyendo casos válidos e inválidos, así como las condiciones de frontera y las propiedades de idempotencia e invariancia de formato.
El pipeline de integración continua (CI/CD) se ejecutó correctamente, con estado verde y artefacto de cobertura publicado.

## 6. Discusión crítica
- Rutas a vigilar: Entradas con caracteres unicode raros; separadores distintos a espacio/guion.
- Recomendación: Añadir Hypothesis para property-based testing más exhaustivo.

## 7. Evidencias
Revisar dentro de la carpeta "coverage_html" el archivo index.html y el archivo "evidencias.json" para detalles completos.

## 8. Referencias
- ISO. (2017). ISO 2108:2017 — International Standard Book Number (ISBN).
- ISBN. Wikipedia.
- Python Software Foundation. Built-in Types — str.
- pytest documentation.
- coverage.py documentation.
- GitHub Actions — guide for Python.
- Hypothesis — property-based testing for Python.

## 9. Anexos
- Comandos para reproducir: "coverage run -m pytest -q" y "coverage html -d coverage_html".
