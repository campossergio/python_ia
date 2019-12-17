print('Estruturas Condicionais')

x = int(input('Digite um número: '))

if x == 10:
    print('Você tirou nota 10')
elif x == 9:
    print('Você tirou nota 9')
elif x < 9:
    print('Você tirou menos de 9')
else:
    print('Digite um valor de 0 até 10')

n1 = 10
n2 = 9

if n1 == 10 and n2 == 9:
    print('Você tirou uma nota 10 "E" uma nota 9')

if n1 == 10 or n2 == 9:
    print('Você tirou uma nota 10 "OU" uma nota 9')

