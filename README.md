# Tarea: Comparación de rendimiento entre CYK y ANTLR4

## Descripción
Implementación y comparación empírica del algoritmo CYK (O(n³)) vs un parser generado con ANTLR4 (O(n)) para reconocer el lenguaje `a^n b^n`.

## Estructura del proyecto

```
.
├── cyk.py                    # Implementación del algoritmo CYK
├── gramatica_antlr.g4        # Gramática ANTLR4 para a^n b^n
├── antlr_ejecutar.py         # Script para ejecutar parser ANTLR4
├── comparar.py               # Script de benchmark y generación de gráfica
├── comparacion.png           # Gráfica de resultados (generada)
└── README.md                 # Este archivo
```

## Requisitos previos

- Python 3.12+
- ANTLR4 (4.13.2)
- Entorno virtual Python (recomendado)

## Instalación y configuración

```bash
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install antlr4-python3-runtime matplotlib

# Generar parser ANTLR4
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 gramatica_antlr.g4
```

## Ejecución

### Probar individualmente cada parser

```bash
python cyk.py aabb           # CYK
python antlr_ejecutar.py aabb # ANTLR4
```

### Ejecutar benchmark completo

```bash
python comparar.py
```

## Resultados obtenidos

| n | Cadena    | Longitud | CYK (ms) | ANTLR4 (ms) |
|---|-----------|----------|----------|-------------|
| 2 | aabb      | 4        | 0.031    | 0.653       |
| 5 | aaaaabbbbb| 10       | 0.167    | 0.736       |
| 10| a...b (20)| 20      | 1.125    | 0.917       |
| 20| a...b (40)| 40      | 8.393    | 1.177       |

## Conclusiones

- **CYK**: Complejidad O(n³) - el tiempo crece aproximadamente 8 veces al duplicar la entrada.
- **ANTLR4**: Complejidad O(n) - el tiempo se mantiene casi constante para los tamaños probados.

Estos resultados confirman la teoría: los parsers lineales son mucho más eficientes para lenguajes de programación reales, aunque requieren gramáticas no ambiguas y sin recursión izquierda (en el caso de ANTLR).


