import re

text = "OneBitCode: Transformamos pessoas em programadores sem limites"

#1 - Indice inicial e final de palavras
# O "r" significa que estamos trabalhando com uma string bruta (raw string)
match = re.search(r"pessoas em programadores", text)
print ("indice inicial ", match.start())
print ("indice final ", match.end())

# 2 - Buscando o incide que possui o ponto
site = "https://onebitcode.com"
match = re.search(r'\.', site)
print(match)


#3 - buscando uma lista de caracteres dentro de uma frase
pattern = "[a-m]"
result = re.findall(pattern, text)
print(text)
print(result)


#4 - verificando o inicio de uma string, se começa com algum padrao
rule = r'^Vam'
phrases = ["A casa está suja", "O dia está lindo", "Vamos passear"]
for f in phrases:
    if re.match(rule, f):
        print(f"Corresponde: {f}")
    else:
        print(f"Não corresponde: {f}")


#4 - verificando o final de uma string, se começa com algum padrao
rule_end = r'!$'
phrases2 = "Vamos passear!"
match = re.search(rule_end, phrases2)
if match:
    print("Sim, corresponde")
else:
    print("Não corresponde!")