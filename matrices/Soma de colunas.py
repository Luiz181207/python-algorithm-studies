#soma de colunas
from random import randint
mat33 = []
for i in range(0,3):
    mat33.append([])
    for j in range(0,3):
        mat33[i].append(randint(0,10))

for i in range(len(mat33)):
    print(mat33[i])

print("Soma das colunas:")
for i in range(0,3):
    s = 0
    for j in range(0,3):
        s += mat33[j][i]
    print(f"soma: {s}")