'''
upper() - deixa todas as letras em maisculas
lower() - deixa todas as letras em minusculas
len() - mostra quantas letras tem na variável
replace('primeira', 'segunda') - troca a primeira parte pela segunda
count('str') - conta quantas letras determinadas tem na string 's'
find('str') - encontra determinada letra e mostra a posição que ela está
title() - deixa todas as inicais das palavras em maiusculas
'''

nome = 'sergio CAMPOS'
nome = nome.upper()
print(nome)

nome = nome.lower()
print(nome)

print(len(nome))

nome = nome.replace('sergio', 'marcia')
print(nome)

print(nome.count('s'))

print(nome.find('a'))

nome = nome.title()
print(nome)