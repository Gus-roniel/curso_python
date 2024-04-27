"""
Criar um input pedindo o nome, ano de nascimento e altura
Definir as variaveis
dar print em cada uma delas para que sejam na ordem STRING, INT e FLOAT
criar um input com a frase 
Olá {nome}! Você tem {idade} anos de idade e tem {altura_em_float} de altura
"""

nome = input("Qual seu nome? ")
ano_de_nascimento = input("Qual seu ano de nascimento? ")
altura = input("Qual sua altura? ")
ano_atual = 2024

ano_de_nascimento_int = int(ano_de_nascimento)
altura_float = float(altura)

print(type(nome))
print(type(ano_de_nascimento_int))
print(type(altura_float))

idade = ano_atual - ano_de_nascimento_int

print(f"Olá {nome}! Você tem {idade} anos de idade e tem {altura_float} de altura.")
