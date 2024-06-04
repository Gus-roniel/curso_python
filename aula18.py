# TRY / EXCEPT / FINALLY / ELSE
# Usado para tratativa de erros
# Except = pode ter diversos erros

while True:
    try:
        numero = float(input('Digite um número '))
        calculo = 10 / numero
        print(calculo)
    except ValueError:
        print('Digite apenas números')
    except ZeroDivisionError:
        print('Não é possível dividir por zero')
    except:
        print('Erro desconhecido')
    else:
        print('Aqui foi executado o else')
    finally:
        print('Aqui houve um finally')


# ValueError
# ZeroDivisionError
