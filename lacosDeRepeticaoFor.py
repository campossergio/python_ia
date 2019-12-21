# TRATAMENTO DE EXCEÇÃO
try:
    x = int(input('Digite sua idade'))
except:
    print('Você não digitou sua idade')
else:
    print(f'sua idade é {x}')
finally:
    print('muito obrigad opor acessar nosso site')

# LAÇOS DE REPETIÇÃO: FOR
x = ['Sergio', 'Campos']

for i in x:
    print(i);

for i in range(1, 1001):
    print(i);

for i in range(0, 1002, 2):
    print(i)