import sys
import time
from antlr4 import *
from gramatica_antlrLexer import gramatica_antlrLexer
from gramatica_antlrParser import gramatica_antlrParser

def parse_with_antlr(cadena):
    input_stream = InputStream(cadena)
    lexer = gramatica_antlrLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gramatica_antlrParser(stream)
    start = time.perf_counter()
    tree = parser.s()
    end = time.perf_counter()
    errors = parser.getNumberOfSyntaxErrors()
    aceptada = (errors == 0)
    return aceptada, (end - start) * 1000

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python antlr_ejecutar.py <cadena>")
        sys.exit(1)
    cadena = sys.argv[1]
    aceptada, tiempo_ms = parse_with_antlr(cadena)
    print(f"Aceptada: {aceptada}")
    print(f"Tiempo ANTLR: {tiempo_ms:.3f} ms")
