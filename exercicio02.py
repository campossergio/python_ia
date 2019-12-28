'''
    FAÇA UM PROGRAMA QUE MOSTRE O RESULTADO DE N!
    5! = 5 * 4 * 3 * 2 * 1 = 120
'''

num = int(input('Digite um número para saber o seu fatorial: '))
print(f'O fatorial de {num} é:')
fat = 1
while num >= 1:
    fat = fat * num
    num -= 1

print(fat)

num02 = int(input('Digite um número: '))
fatorial = 1
for x in range(num02, 0, -1):
    fatorial = fatorial * x

print(fatorial)

for y in range(1, 10):
    print(y)