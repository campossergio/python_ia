## FUNÇÕES ##

''' PARA CRIAR FUNÇÕES DEVEMOS SEMPRE USAR A PALAVRA RESERVADA "def" '''

def mostrarNaTela():
    print('Hello World!!!')
    print('Fim do Programa...')

''' CHAMANDO A FUNÇÃO '''
mostrarNaTela()

def somarNumeros(n1, n2):
    print(f'A soma dos números é {n1 + n2}')

somarNumeros(5, 10)

''' EMPACOTAMENTO DE PARAMETROS - USANDO TUPLA () '''
def retornarMaior(*list):
    print('O maior valor é: {}'.format(max(list)))
    print('O menor valor é: {}'.format(min(list)))
    print('A soma total dos valores é: {}'.format(sum(list)))


retornarMaior(12, 98, 646, 548, 124)


