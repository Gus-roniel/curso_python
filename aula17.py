# REPETIÇÕES

# WHILE
# Executa uma ação enquanto uma condição for verdadeira
# Loop infinito - quando um código não tem fim


contador = 1
while contador <= 100:
    contador = contador + 1

    if contador == 10:
        print('pulando o numero 10')
        continue

    if contador == 40:
        break
    print(contador)
