from random import randint
"""Encontre o maior elemento de um vetor"""
vet = []

for i in range(10):
    num = randint(0,50)
    vet.append(num)

"""print(f"Vetor: {vet},\n"
      f"maior número: {max(vet)}")
      ou:
    """

maior_elem = 0
for i in range(len(vet)):
    if vet[i] > maior_elem:
        maior_elem = vet[i]

print(f"Vetor: {vet}, \n"
      f"Maior elemento: {maior_elem}")
