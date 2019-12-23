'''
append - adicionar elementos dentro de uma lista sempre ma última posição
insert(0, 'x') - adiciona elementos na posição escolhida
pop(1) - sem parametro(indice) remove a última posição da lista
remove('x') - remove um item da lista pelo valor
len() - mostra a quantidade de elementos de uma lista
sort() - ordena a lista de forma crescente
reverse - ordena de forma decrescente

max() - mostra o maior valor
min() - mostra o menor valor
sum() - mostra a soma dos valores

'''

''' LISTAS x = [] or x = list[] '''
idade = [10, 20, 30, 40, 50, 70, 15, 25, 35, 55, 45,]

idade.append(18)
print(idade)

idade.insert(1 , 25)
print(idade)

idade.pop()
print(idade)

idade.pop(1)
print(idade)

idade.remove(10)
print(idade)

print(len(idade))

idade.sort()
print(idade)

idade.sort(reverse = True)
print(idade)

idade2 = [1, 2, 3, 4, 5]
print(idade2)

idade2.reverse()
print(idade2)

print(max(idade))

print(min(idade))

print(sum(idade))

''' LISTAS PARTE 2 IN FOR IF '''

x = []

for i in range(1, 11):
    x.append(i)

print(x)

y = list(range(1, 16))
print(y)

''' VERIFICAR SE O VALOR ESTÁ CONTIDO NA LISTA '''

z = int(input('Digite um número da lista "Y" para remover'))

if z in y:
    y.remove(z)
    print('O valor foi removido com sucesso...')
else:
    print('Este valor não está contido na lista')
    z = int(input('Digite um valor da lita'))
    print(y)
    y.remove(z)

print(y)

''' LISTAS DE LISTAS '''

nomeIdade = [['sergio', 41], ['marcia', 45], ['giovani', 14], ['miguel', 6]]
print(nomeIdade)

print(nomeIdade[0][0])

''' DICIONÁRIO {} or dict'''

nome = {'nome': 'sergio', 'idade': 41}
print(nome)
print(nome['nome'])

cadastro = [{'nome': 'sergio', 'idade': 41}, {'nome': 'marcia', 'idade': 45}]
print(cadastro[0]['idade'])

print(cadastro)

