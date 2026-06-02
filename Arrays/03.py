"""Crie um vetor contendo N elementos digitados pelo usuário"""

lista = []
print("Digite p para parar")

a = 0

while a == 0:
    n = (input("Digite um número:")).lower()
    if n == "p":
        print(lista)
        a = 1
    else:
        n = int(n)
        lista.append(n)