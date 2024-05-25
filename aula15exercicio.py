# Programa para inscrição em um evento
# Pessoa deve ter pelo menos 18 anos
# Deve ser sócia do clube ou ter sido convidada

# Solicita as informações do usuário
#   nome
#   idade
#   socia?
#   convidada?
nome = input('Qual seu nome? ').capitalize()
idade = int(input("Digite sua idade: "))
tem_vip = input("Você possui ingresso VIP? (sim/nao): ").strip().lower()
membro_clube = input("Você é membro do clube? (sim/nao): ").strip().lower()

# Verifica se a pessoa pode se inscrever no evento
# idade minima
if idade < 18:
    print("Você não pode se inscrever no evento. Idade mínima é 18 anos.")
# é sócia ou foi convidada para o evento
elif tem_vip == "sim" or membro_clube == "sim":
    print(f"Você pode se inscrever no evento {nome} .")
else:
    print(f"Desculpe {
          nome}, Você não atende aos requisitos para se inscrever no evento.")
