'''
    FAÇA UM PROGRAMA QUE VERIFIQUE E MOSTRE OS NÚMEROS ENTRE 1000 E 2000(INCLUSIVE)
    QUE, QUANDO DIVIDIDO POR 11 PRODUZ RESTO IGUAL A 5
'''

for x in range(1000, 2001):
    if x % 11 == 5:
        print(x)
    else:
        continue

