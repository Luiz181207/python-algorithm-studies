from random import randint
mat33 = []
for i in range(0,3):
    mat33.append([])
    for j in range(0,3):
        mat33[i].append(randint(0,10))

for i in range(len(mat33)):
    print(mat33[i])

s = 0
for i in range(0,3):
    for j in range(0,3):
        if i == j:
            s += mat33[i][j]
print(s)