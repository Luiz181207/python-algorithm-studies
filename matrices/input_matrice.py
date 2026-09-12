mat3x3 = []
print("digite os 9 números da matriz:")

for i in range(3):# cria 3 linhas
    linha = []
    for j in range(3):#3 elementos por linha
        n = int(input(f"digite o elemento [{i+1}][{j+1}]:"))
        linha.append(n)
    mat3x3.append(linha)

print("matriz 3x3:")
for linha in (mat3x3):
    for x in (linha):
        print("|", f"\t{x}\t", "|", end = "") #escreve os elementis na mesma linha(end="" impede o print de pular pra próxima linha
    print()#quando acaba as os "x" da linha pula pra próxma linha e imprime os elementos da próxima linha