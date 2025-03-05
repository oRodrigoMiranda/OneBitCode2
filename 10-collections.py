from collections import Counter, namedtuple, deque
from operator import itemgetter

#1 - Contar itens de uma lista
fruits = ["Maçã", "Banana", "Uva", "Pêra", "Uva", "Maçã", "Laranja", "Abacaxi", "Tangerina", "Uva", "Pêra", "Banana"]
print(fruits)
print(Counter(fruits))

#2 - utilizando tupla nomeada
game = namedtuple('game', ['name','price','note'])
g1 = game("Fifa25", 200, 7)
g2 = game("Resident Evil 4 Remake", 200, 9)
print(g1)
print(g2)

#3 - ordenando dicionários
students = {"Pedro":23, "Ana":22, "Ronaldo":26, "Janaina":25}
a = sorted(students.items(), key=itemgetter(0))
print(students)
print(a)

#4 - Utilizando filas ambas extremidades
deq = deque([20, 40, 60, 80])
deq.appendleft(10)
print(deq)
deq.append(90)
print(deq)
deq.popleft()
deq.pop()
print(deq)
