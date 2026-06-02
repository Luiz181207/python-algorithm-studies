"""Crie dois vetores de 5 elementos cada, e posteriormente crie um terceiro resultante da soma deste dois"""
import random

vet1 = []
vet2 = []

for i in range(5):
    num = random.randint(0,10)
    vet1.append(num)

for i in range(5):
    num = random.randint(0,10)
    vet2.append(num)

print(f"Vetor 1: {vet1}\n"
      f"Vetor 2: {vet2}")

tam = len(vet1)
vet3 = []

for i in range(tam):
    soma = vet1[i] + vet2[i]
    vet3.append(soma)

print(f"Soma dos vetores 1 à 1: {vet3}")