# CONDICIONAIS
# if, elif, else

idade = int(input('Digite a sua idade: '))
idade_para_dirigir = 18

if idade < idade_para_dirigir:
    print('Você ainda não pode tirar CNH')
else:
    print('Você já pode fazer CNH')


idade2 = int(input('Digite sua idade: '))
casar_com_autorizacao = 16
idade_para_casar = 18
if idade2 < casar_com_autorizacao:
    print('Você ainda não pode casar')
elif idade2 >= casar_com_autorizacao and idade2 < idade_para_casar:
    print('Pode casar com autorização dos pais')
else:
    print('Pode casar')
