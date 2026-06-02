"""Crie um vetor contendo N elementos pares digitados pelo usuário"""

lista = []
print("Digite p para parar")

a = 0
while a == 0:
    n = input("Digite um número:").lower()
    if n == "p":
        print(f"Números pares digitados:\n {lista}")
    else:
        n = int(n)
        if n % 2 == 0:
            lista.append(n)

