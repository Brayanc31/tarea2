import sys
import time

def cyk_parse(cadena):
    # Gramática FNC correcta para a^n b^n (n>=1)
    # S -> A S1 | A B
    # S1 -> S B
    # A -> a
    # B -> b
    grammar = {
        'S': [('A','S1'), ('A','B')],
        'S1': [('S','B')],
        'A': ['a'],
        'B': ['b']
    }
    tokens = list(cadena)
    n = len(tokens)
    if n == 0:
        return False  # n>=1
    P = [[set() for _ in range(n)] for _ in range(n)]
    
    # Inicializar terminales
    for i, tok in enumerate(tokens):
        for lhs, rhs_list in grammar.items():
            for rhs in rhs_list:
                if isinstance(rhs, str) and rhs == tok:
                    P[i][i].add(lhs)
    
    # Subcadenas de longitud >= 2
    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                for lhs, rhs_list in grammar.items():
                    for rhs in rhs_list:
                        if isinstance(rhs, tuple) and len(rhs) == 2:
                            B, C = rhs
                            if B in P[i][k] and C in P[k+1][j]:
                                P[i][j].add(lhs)
    return 'S' in P[0][n-1]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python cyk.py <cadena>")
        sys.exit(1)
    cadena = sys.argv[1]
    start = time.perf_counter()
    aceptada = cyk_parse(cadena)
    end = time.perf_counter()
    tiempo_ms = (end - start) * 1000
    print(f"Aceptada: {aceptada}")
    print(f"Tiempo CYK: {tiempo_ms:.3f} ms")
