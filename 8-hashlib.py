import hashlib

#1 - verificar os algoritmos disponiveis
#print(hashlib.algorithms_available)

#2 - verificar os algoritmos disponiveis de acordo com o SO
#print(hashlib.algorithms_guaranteed)

#3 - utilizando o Sha256
algorithm = hashlib.sha256()
print(algorithm.digest())
message = "A melhor forma de prever o futuro é criá-lo".encode()
algorithm.update(message)
print(f'sha256 = {algorithm.hexdigest()}')

#4 - utilizando o md5
md5 = hashlib.md5()
md5.update(message)
print(f'md5 = {md5.hexdigest()}')