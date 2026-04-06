import subprocess
import matplotlib.pyplot as plt

def medir_cyk(cadena):
    proc = subprocess.run(['python3', 'cyk.py', cadena], capture_output=True, text=True)
    for line in proc.stdout.split('\n'):
        if 'Tiempo CYK' in line:
            return float(line.split(':')[1].strip().split()[0])
    return None

def medir_antlr(cadena):
    proc = subprocess.run(['python3', 'antlr_ejecutar.py', cadena], capture_output=True, text=True)
    for line in proc.stdout.split('\n'):
        if 'Tiempo ANTLR' in line:
            return float(line.split(':')[1].strip().split()[0])
    return None

ns = range(2, 21)  # n desde 2 hasta 20 (cadenas de longitud 4 a 40)
tiempos_cyk = []
tiempos_antlr = []
valores_n = []

print("Ejecutando benchmark...")
for n in ns:
    cadena = 'a'*n + 'b'*n
    print(f"Probando n={n}, longitud={2*n}")
    t_cyk = medir_cyk(cadena)
    t_antlr = medir_antlr(cadena)
    if t_cyk is not None:
        tiempos_cyk.append(t_cyk)
        valores_n.append(n)
    if t_antlr is not None:
        tiempos_antlr.append(t_antlr)

plt.figure(figsize=(10,5))
plt.plot(valores_n[:len(tiempos_cyk)], tiempos_cyk, 'o-', label='CYK (O(n³))')
plt.plot(valores_n[:len(tiempos_antlr)], tiempos_antlr, 's-', label='ANTLR4 (O(n))')
plt.xlabel('n (tamaño de a^n b^n)')
plt.ylabel('Tiempo (ms)')
plt.title('Comparación de rendimiento: CYK vs ANTLR4')
plt.legend()
plt.grid(True)
plt.savefig('comparacion.png')
plt.show()

print("\nResultados numéricos:")
print("n\tCYK (ms)\tANTLR4 (ms)")
for i, n in enumerate(valores_n[:len(tiempos_cyk)]):
    cyk_val = tiempos_cyk[i] if i < len(tiempos_cyk) else 'N/A'
    antlr_val = tiempos_antlr[i] if i < len(tiempos_antlr) else 'N/A'
    print(f"{n}\t{cyk_val:.3f}\t\t{antlr_val:.3f}")
