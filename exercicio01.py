'''
    FAÇA UM PROGRAMA QUE RECEBA O PESO DE 7 PESSOAS.
    CALCULE E MOSTRE:
        A QUANTIDADE DE PESSOAS ACIMA DE 90KG;
        A MÉDIA DOS PESOS DAS PESSOAS.
'''

peso = 0
pessoas = 1
pesoTotal = []
acimaDoPeso = 0
media = 0

while pessoas <= 7:
    peso = float(input('Digite seu peso: '))

    if peso >= 90:
        acimaDoPeso += 1

    pesoTotal.append(peso)

    pessoas += 1

media = sum(pesoTotal) / 7

print(f'{acimaDoPeso} pessoas estão com peso acima de 90kg')
print('O peso de cada pessoa é: {}'.format(pesoTotal))
print('O peso médio dessas pessoas é: {:.2f}'.format(media))


''' OUTRA SOLUÇÃO 
    x = []
    contador = 0
    for i in range(0, 7):
        x.append(float(input('Digite seu peso: ')))
        if x[i] > 90:
            contador += 1
            
    print(f'existem {contador} pessoas acima de 90kg e media dos pesos é {sum(x}/len(x):.2f}'        
'''

