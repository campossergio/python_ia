''' ARQUIVOS - COMO TRABALHAR COM ARQUIVOS EM PYTHON
    CRIAR VARIÁVEL
    OPEN - PARA ABRIR O ARQUIVO
    NOME DO ARQUIVO - ARQUIVO.TXT OU OUTRO
    W - ESCREVER
    R - LER
    A - ALTERAR
    READLINES - LÊ LINHA POR LINHA

    NO FINAL SEMPRE FECHAR O ARQUIVO

    "SE O ARQUIVO NÃO EXISTIR ELE SERÁ CRIADO AUTOMÁTICAMENTE"
'''


arquivo = open('aulaPython.txt', 'r')

texto = ''' Meu nome eh Sergio e
    estou estudando a linguagem Python...
'''

#arquivo.write(texto)
#lerArquivo = arquivo.read()

lerArquivo = arquivo.readlines()

for i in lerArquivo:
    print(i)

arquivo.close




