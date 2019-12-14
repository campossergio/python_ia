print('Introdução a Programação com Python')
print('Aula 01 - Variáveis')

nome = 'Sérgio Campos'
idade = 41

print(f'Meu nome é {nome} e tenho {idade} anos.')

print('Meu nome é {} e tenho {} anos'.format(nome, idade))

print('Meu nome é {z} e tenho {y} anos'.format(z=nome, y=idade))

# f significa que estou formatando o print e colocando a variável entre chaves {}

# mostrando o tipo de variável
print(type(idade))
print(type(nome))
print(type(True))