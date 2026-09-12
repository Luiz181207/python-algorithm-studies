#4x3:
from random import randint
"""mat = [[10,64,12],
       [80,32,1],
       [56,122,456],
       [700,-123,90]]

print(mat)
for i in range(0,4):
    print(f"linha {i}: {mat[i]}")
    for j in range(0,3):
        print(f"{i},{j},: {mat[i][j]}")"""


mat = []
for i in range(0,6):
    mat.append([])
    for j in range(0,3):
        mat[i].append(randint(0,100))

print(mat)
