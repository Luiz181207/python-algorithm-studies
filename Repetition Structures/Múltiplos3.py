# Escreva um programa que exiba os múltiplos de 3 de 0 a 100.
print(10 * '<', 'Múltiplos de 3', 10 * '>')
n = 0
while n <=100:
    if n % 3 == 0:
        print(n)
    n += 1