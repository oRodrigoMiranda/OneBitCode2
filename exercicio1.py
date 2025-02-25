def reverse(string):
    return string[::-1]

def letras_pares(string):
    pares = ""
    for i, char in enumerate(string):
        if i % 2 == 0:
            pares += char
    return pares

def letras_impares(string):
    impares = ""
    for i, char in enumerate(string):
        if i % 2 != 0:
            impares += char
    return impares

def letra_impar(string):
    return string[1::2]


print (reverse("Celso"))
print (letras_pares("Bolo"))
print (letras_impares("Bolo"))
print (letra_impar("Bolo"))