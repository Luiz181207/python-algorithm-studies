from random import randint
mat75 = []
for i in range(7): #cria 7 linhas
    linha = []
    for j in range (5):
        linha.append(randint(0,35))
    mat75.append(linha)

print("Matriz 7x5:")
for linha in (mat75):
    for x in (linha):
        print(f"| \t{x}\t |", end = "")
    print()

