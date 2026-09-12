#Escreva um programa que gere um número aleatório entre 1 e 100 e peça para o usuário adivinhá-lo.
import random
from time import sleep

n = random.randint(1,100)
tentativas = 10


nuser = -1
while nuser != n:
    nuser = int(input('Digite um número:'))
    if tentativas == 0:
        print('\033[1;31mVocê perdeu!!')
        print(f'O número era {n}')
        exit()
    elif nuser == n:
        print('\033[1;32mParabéns, você acertou!\n'
              f'Você utilizou {11 - tentativas} tentativas')
    elif nuser < n:
        print('Tente um número maior')

    elif nuser > n:
        print('Tente um número menor')


    tentativas -= 1


