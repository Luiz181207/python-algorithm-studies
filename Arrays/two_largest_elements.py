"""Encontre os dois maiores elementos de um vetor"""
from random import randint

vet = []
for i in range(15):
    num = randint(0,50)
    vet.append(num)

maior_elem = 0
seg_maior = 0

for i in range(len(vet)):
    if vet[i] > maior_elem:
        maior_elem = vet[i]
    if vet[i] > seg_maior and vet[i] < maior_elem:
        seg_maior = vet[i]

print(f"Vetor: {vet}\n"
      f"Maior elemento: {maior_elem}\n"
      f"2º maior: {seg_maior}")
