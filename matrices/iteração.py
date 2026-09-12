#criando uma matriz 5x3 utilizando números aleatórios
from random import randint

mat2d = []

for i in range(0,5):
    mat2d.append([])
    for c in range(0,3):
        num = randint(0,50)
        mat2d[i].append(num)

print(mat2d)