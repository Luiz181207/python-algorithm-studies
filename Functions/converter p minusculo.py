def lower_(text):
    new_text = ""
    for letra in text:
        asc = ord(letra)
        if asc >= 65 and asc <= 90:
            asc += 32
        asc = chr(asc)
        new_text += asc
    return new_text

texto = "LuiIZ FelipE FerNANdEAs"
print(lower_(texto))