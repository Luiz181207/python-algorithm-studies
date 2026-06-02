"""Apresente a soma dos elementos opostos de um vetor de 100 elementos"""

soma = 0

vetor = [i+1 for i in range(100)]

for c in range(50):
    soma += vetor[c] + vetor[99 - c]

print(f"A soma dos opostos é: {soma}")
