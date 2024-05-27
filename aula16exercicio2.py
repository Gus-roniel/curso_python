"""
Exercício: Avaliação de Rendimento Escolar

Você é responsável avaliar o rendimento escolare as regras para determinar a situação de um aluno são as seguintes:

Se a média das 3 notas do aluno forem maiores ou igual a 7, o aluno está "Aprovado" independente do número de faltas.
Se a média das notas do aluno forem maiores ou igual a 5, mas ele tiver 5 ou mais faltas, o aluno está "Em Recuperação". Se tiver menos de 5 faltar aluno aprovado
Se a média das notas do aluno for menor que 5, o aluno está "Reprovado".

Passos:
Crie variáveis para armazenar a média das notas do aluno e o número de faltas.
Criar 3 variaveis para cada nota, e uma para resultado final
criar uma variavel com numero de faltas do aluno
Use uma estrutura condicional if-elif-else para verificar as regras de avaliação.
Imprima a situação do aluno.
"""
nota_1 = float(input('Insira o valor da primeira nota \n(valor de 1 a 10)\n '))
nota_2 = float(input('Insira o valor da segunda nota '))
nota_3 = float(input('Insira o valor da terceira nota '))
numero_de_faltas = int(input('Quantas faltas o aluno teve? '))

media = round(((nota_1+nota_2+nota_3) / 3), 3)
# Insira o valor da primeira nota 6.21
# Insira o valor da segunda nota 4.61
# Insira o valor da terceira nota 5.23
# Quantas faltas o aluno teve? 8

if media >= 7:
    print(f'Aluno aprovado com nota {media}')
elif media < 5:
    print(f'Aluno reprovado com nota {media}')
elif media >= 5 and numero_de_faltas >= 5:
    print(f'Aluno ficou em recuperação com nota {media}')
elif media >= 5 and numero_de_faltas < 5:
    print(f'Aluno ficou foi aprovado com nota {media}')
