# Laços de Repetição - WHILE

x = 0

while x <= 10:
    print(x)
    x += 1

print('acabou o laço!')

decisao = 0

while decisao != 3:
    decisao = int(input('Digite 1 para logar, 2 para cadastrar, 3 para sair'))

    if decisao == 1:
        print('logando...')
    elif decisao == 2:
        print('cadastrando!!!')
    elif decisao == 3:
        print('saindo....')

print('Obrigado, Volte Sempre!!!!1')

#LAÇOS DE REPETIÇÃO : WHILE PARTE 2
x = -1

while x < 11:
    x += 1
    if x == 5:
        continue

    print(x)

print('acabou a laço!!!');
