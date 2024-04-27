"""
Criar um input pedindo o nome, ano de nascimento e altura
Definir as variaveis
dar print em cada uma delas para que sejam na ordem STRING, INT e FLOAT
criar um input com a frase 
Olá {nome}! Você tem {idade} anos de idade e tem {altura_em_float} de altura
"""












nome = input("Qual seu nome? ")
ano_de_nascimento = input("Qual seu ano de nascimento? ")
altura = input("Qual seu tamanho? ")
ano_atual = 2024

idade = ano_atual - int(ano_de_nascimento)
altura_em_float = float(altura)

print(type(nome))
print(type(idade))
print(type(altura_em_float))

print(f"Olá {nome}! Você tem {idade} anos de idade e tem {altura_em_float} de altura")



