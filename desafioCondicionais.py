'''
Criar um programa que receba o Nome do Aluno
    Idade
    Nota 01
    Nota 02

    Retornar o nome com as iniciais em Maiusculas
    verificar de a idade é maior ou igual à 18
    média das notas maior ou igual à 6
    retornar Aprovado
    média menor que 6
    retornar Reprovado
'''

print('Desafio Notas do Aluno')

aluno = input('Digite seu nome: ')
idade = int(input('Digite sua Idade: '))
n1 = float(input('Digite a nota da Primeira Prova: '))
n2 = float(input('Digite a nota da Segunda Prova: '))

media = (n1 + n2) / 2

print(aluno.title())

if idade >= 18 and media >= 6:
    print(f'Sua idade é {idade} e Sua média final é {media}')
    print('Aprovado!!!')
elif idade < 18 or media < 6:
    print('Sua Idade é: {} e Sua Média Final é {}'.format(idade, media))
    print('Reprovado!!!')