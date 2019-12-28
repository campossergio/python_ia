'''
    FAÇA UM PROGRAMA QUE RECEBA VÁRIAS IDADES E CALCULE E MOSTRE A MÉDIA DAS IDADES.
    FINALIZE O PROGRAMA QUANDO A ENTRADA FOR IGUAL À -1
'''
somaIdade = []
idade = 0

while idade != -1:
    idade = int(input('Digite sua idade: '))
    if idade == -1:
        break
    else:
        somaIdade.append(idade)

media = sum(somaIdade) / len(somaIdade)
print('A média das idades é {} anos'.format(media))