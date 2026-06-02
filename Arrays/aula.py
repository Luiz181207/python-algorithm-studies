plv = "Bom dia"

tam = len(plv)
print(f"{plv} tem {tam} caracteres")

"""for i in range(tam):
    n_ascii = ord(plv[i]) #ord coverte o caractere em número ordinal
    print(f"{i+1}-{plv[i]}-{n_ascii}")"""

cesar_key = 10
code_plv = []

for i in range(tam):
    n_ascii = ord(plv[i])
    print(f"{plv[i]}, {n_ascii}")
    code = n_ascii + cesar_key
    letter_code = chr(code)
    code_plv.append(letter_code)

print(f"{plv} = {code_plv}")