from random import randint
#2x2:
mat2 = []
for i in range(0,2):
    mat2.append([])
    for j in range(0,2):
        mat2[i].append(randint(0,10))
print("Matriz 2x2:")
for i in range(len(mat2)):
    print(mat2[i])
print()

#5x3:
mat53 = []
for i in range(0,6):
    mat53.append([])
    for j in range(0,4):
        mat53[i].append(randint(0,10))
print(f"Matriz 5x3:")
for i in range(len(mat53)):
    print(mat53[i])
print()

#10x5:
mat105 = []
for i in range(0,11):
    mat105.append([])
    for j in range(0,6):
        mat105[i].append(randint(0,10))
print(f"Matrix 10x5:")
for i in range(len(mat105)):
    print(mat105[i])