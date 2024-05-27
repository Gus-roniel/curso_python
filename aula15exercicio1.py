# Programa para inscrição em um evento
# Pessoa deve ter pelo menos 18 anos
# Deve ser sócia do clube ou ter sido convidada

# Solicita as informações do usuário
#   nome
nome = input('Qual seu nome? ').capitalize()
#   idade
idade = int(input('Digite sua idade: '))
#   socia?
e_socia = input('Você é membro(a) do clube? [sim] ou [não]')
#   convidada?
e_convidada = input('Você foi convidado(a) para o evento? [sim] ou [não]')

# Verifica se a pessoa pode se inscrever no evento
# idade minima
if idade < 18:
    print(f'Desculpe {nome}, você não pode participar. Tem menos de 18 anos')

# é sócia ou foi convidada para o evento
elif e_socia == 'sim' or e_convidada == 'sim':
    print(f'Seja bem vindo {nome}. Você pode fazer sua inscrição.')

else:
    print(f'Desculpe {nome}, você não pode participar do evento.')


# nome = input('Qual seu nome? ').capitalize()
# idade = int(input("Digite sua idade: "))
# tem_vip = input("Você possui ingresso VIP? (sim/nao): ").strip().lower()
# membro_clube = input("Você é membro do clube? (sim/nao): ").strip().lower()

# # Verifica se a pessoa pode se inscrever no evento
# # idade minima
# if idade < 18:
#     print("Você não pode se inscrever no evento. Idade mínima é 18 anos.")
# # é sócia ou foi convidada para o evento
# elif tem_vip == "sim" or membro_clube == "sim":
#     print(f"Você pode se inscrever no evento {nome} .")
# else:
#     print(f"Desculpe {
#           nome}, Você não atende aos requisitos para se inscrever no evento.")
