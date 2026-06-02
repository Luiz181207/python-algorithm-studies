"""Crie um vetor de 20 elementos aleatórios"""

import random

lista = []

for i in range (0, 21):
    vet = random.randint(0,100)
    lista.append(vet)

print(lista)
