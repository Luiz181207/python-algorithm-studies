def upper_(texto):
    novo_texto = ""
    for letra in texto:
        asc = ord(letra)
        if asc >= 97 and asc <= 122:
            asc -= 32
        asc = chr(asc)
        novo_texto += asc
    return novo_texto

texto = "MaraiM anbhLLOH"
print(upper_(texto))