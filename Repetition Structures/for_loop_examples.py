#for i in range(30, 15, -2): #o segundo numero limita o período - começa no 30 e vai ate 16
    #print( i)

#for i in range(0,10,1): # vai de 0 á 9
    #print(i)

""""
print('Números pares entre 1 e 100:')
for i in range(0,101,2):
    print(i)
print()

print('Números ímpares entre 1 e 100:')
for i in range(1,101,2):
    print(i)
"""
""""
soma = 0
print('Soma dos múltiplos de 5 entre 1 e 100:')
for i in range(0,101):
    if i % 5 == 0:
        soma += i
    if i % 2 == 0:
        print(f'{i} é par')
    else:
        print(f'{i} é ímpar')

print(f'Soma dos múltiplos de cinco  = {soma}')
"""

from time import sleep
seg = 0
min = 0
hor = 0

while True:
    sleep(1)
    seg +=1
    if seg == 60:
        min += 1
        seg = 0
    if min == 60:
        hor += 1
        min = 0

    print(f'{hor}:{min}:{seg}')
