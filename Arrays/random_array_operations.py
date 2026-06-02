"""Crie um vetor aleatorio. Posteriormente apresente a soma dos pares e depois dos múltiplos de 5. Também, crie um vetor com os múltiplos de 10 do vetor original."""
import random
vetor = []

tam = int(input("Digite a quantidade de elementos desejada: "))

for i in range(tam):
    n = random.randint(0,100)
    vetor.append(n)

print(vetor)

pares = []
fivem = []

for i in range(tam):
    if vetor[i] % 2 == 0:
        pares.append(vetor[i])
    if vetor[i] % 5 == 0:
        fivem.append(vetor[i])

print()
print(f"soma dos elementos pares: {sum(pares)}\n"
      f"Múltiplos de 5: {fivem}")

print("valor máximo: ", max(vetor)) #maior valor
print("valor mínimo: ", min(vetor)) #menor valor
print("soma dos elementos: ", sum(vetor)) #soma dos valores
print("vetor organizado: ", sorted(vetor)) #organiza em valores crescentes
