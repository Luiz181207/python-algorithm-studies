#Escreva um programa que faça a contagem regressiva de 10 a 0.
from time import sleep
print(10 * '<', 'Contagem Regressiva', 10 * '>')

n = 10
while n >= 0:
    print(n)
    n -= 1
    sleep(1)
print('Feliz Ano Novo!!!')
