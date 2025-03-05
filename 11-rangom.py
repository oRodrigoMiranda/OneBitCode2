import random

#1 - seleciona valor aleatorio de uma lista
list1 = [7, 6, 5, 4, 3, 2, 1]
print(random.choice(list1))

#2 - gera um numero aleatório em um intervalo de valores
f1 = random.randint(5,15)
print(f1)

#3 - seleciona caractere aleatório de uma string
name = "Curso Python"
r2 = random.choice(name)
print(r2)

#4 - seleciona mais de um valor aleatorio
#sintaxe: random.sample(sequencia, tamanho)
print(random.sample(list1, 2))
print(random.sample(list1, 3))