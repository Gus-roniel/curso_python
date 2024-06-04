# EXERCÍCIO CALCULADORA

# Crie uma calculadora que peça 2 números e qual operação o usuário deseja
# Ter as 4 operações (+ - / e *)

# Usar while para manter programa funcionando
# Criar o comando sair para encerrar o programa

# Usaremos While, try, except e condicionais


print('SEJA BEM VINDO AO PROGRAMA CALCULADORA')

while True:
    valor_1 = input(
        'Digite a opção "sair" ou digite o primeiro número\n').lower()
    try:
        valor_1_float = float(valor_1)
        valor_2 = float(input('Digite o segundo número\n'))

        operacao = input(
            'Digite a operação desejada:\n+ = soma\n- = subtração\n* = multiplicação\n/ = divisão\n')

        if operacao == "+":
            print(valor_1_float + valor_2)
        elif operacao == "-":
            print(valor_1_float - valor_2)
        elif operacao == "*":
            print(valor_1_float * valor_2)
        elif operacao == "/":
            print(valor_1_float / valor_2)
    except ValueError:
        if valor_1 == 'sair':
            print('Obrigado por usar nossa calculadora!')
            break
        else:
            print('Digite uma opção válida!')
    except ZeroDivisionError:
        print('Não é possível dividir por zero')
    finally:
        ...
