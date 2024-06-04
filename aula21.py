# Métodos de list
# CRUD = Create Read Update Delete

teste = [2, True, 'Gustavo', 1.6]
tes = [2, 4, 5]

print(teste)
# cuidado com o uso de memória
# del
# del teste[1]
# print(teste)
# insert
# teste.insert(1, False)
# print(teste)

# pop (retorna número removido)
d = teste.pop()
print(d)
print(teste)
# append
teste.append('Maria')
print(teste)
print(teste[-1])

# clear
# teste.clear()
# print(teste)

# extend - Mexe na lista original
abc = teste + tes
print(abc)

print(teste)
