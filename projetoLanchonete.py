import matplotlib.pyplot as plt
import pymysql.cursors

conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'lanchonete',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

autentico = False

def logarCadastrar(decidir):
    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False

    if decisao == 1:
        nome = input('Digite seu Nome: \n')
        senha = input('Digite sua Senha: \n')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
                break
            else:
                autenticado = False

        if not autenticado:
            print('email ou senha errada')

    elif decisao == 2:
        print('Faça seu cadastro')
        nome = input('Digite seu Nome: \n')
        senha = input('Digite sua Senha: \n')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                usuarioExistente = 1

        if usuarioExistente == 1:
            print('usuario ja cadastrado tente um nome ou senha diferente')
        elif usuarioExistente == 0:
            with conexao.cursor () as cursor:
                cursor.execute ( 'insert into cadastros(nome, senha, nivel) values(%s, %s, %s)', (nome, senha, 1) )
                conexao.commit ()
                print ( 'usuario cadastrado com sucesso....' )

    return autenticado, usuarioMaster

def cadastrarProdutos():
    nome = input('Digite o nome do Produto: \n')
    ingredientes = input('Digite os ingredientes dos Produtos: \n')
    grupo = input('Digite o grupo pertencente a este Produto: \n')
    preco = float(input('Digite o preço do Produto: \n'))

    # INSERIR OS DADOS NO BANCO, E FAZER O TRATAMENTO DE ERROS
    try:
        with conexao.cursor() as cursor:
            cursor.execute('insert into produtos (nome, ingredientes, grupo, preco) values (%s, %s, %s, %s);', (nome, ingredientes, grupo, preco))
            conexao.commit()
            print('Produto cadastrado com sucesso')
    except:
        print('Erro ao cadastrar os produtos no banco de dados!!!')

def listarProdutos():
    # Criar uma lista com os produtos
    produtos = []

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos;')
            produtosCadastrados = cursor.fetchall()
    except:
        print('Erro ao conectar ao banco de dados')

    for i in produtosCadastrados:
        produtos.append(i)

    if len(produtos) != 0:
        for i in range(0, len(produtos)):
            print(produtos[i])
    else:
        print('Nenhum Produto Cadastrado...')

def excluirProdutos():
    idDeletar = int(input('Digite o ID do Produto que deseja excluir: \n'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('delete from produtos where id = {};'.format(idDeletar))
            conexao.commit()
    except:
        print('Erro ao conectar ao banco de dados!!!')

def listarPedidos():
    pedidos = []
    pedidoCliente = 0

    while pedidoCliente != 2:
        pedidos.clear()

        try:
            with conexao.cursor() as cursor:
                cursor.execute('select * from pedidos;')
                listaPedidos = cursor.fetchall()
        except:
            print()

        for i in listaPedidos:
            pedidos.append(i)

        if len(pedidos) != 0:
            for i in range(0, len(pedidos)):
                print(pedidos[i])
        else:
            print('Nenhum pedido feito....')

        pedidoCliente = int(input('Digite 1 para finalizar Pedido entregue, 2 para voltar'))

        if pedidoCliente == 1:
            idDeletar = int(input('Digite o ID do Pedido entregue: \n'))

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('delete from pedidos where id = {}'.format(idDeletar))
                    print('Pedido entregue!!!')
            except:
                print('Erro ao conectar ao banco de dados para finalizar o pedido.')

# GERANDO GRÁFICOS
def gerarEstatistica():

    nomeProdutos = []
    nomeProdutos.clear()

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from produtos;')
            produtos = cursor.fetchall()
    except:
        print('Erro ao conectar ao banco de dados!!!')

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from estatisticaVendido')
            vendido = cursor.fetchall()
    except:
        print('Erro ao conectar ao banco de dados!!!')

    estado = int(input('Digite 0 para sair, 1 para pesquisar por nome, 2 para pesquisar por grupo'))

    if estado == 1:
        decisao3 = int(input('Digite 1 para pesquisar por dinheiro, 2 para pesquisar por quantidade unitária'))
        if decisao3 == 1:

            for i in produtos:
                nomeProdutos.append(i['nome'])

                valores = []
                valores.clear()

                for h in range(0, len(nomeProdutos)):
                    somaValor = -1
                    for i in vendido:
                        if i['nome'] == nomeProdutos[h]:
                            somaValor += i['preco']
                    if somaValor == -1:
                            valores.append(0)
                    elif somaValor >= 0:
                        valores.append(somaValor+1)

            plt.plot(nomeProdutos, valores)
            plt.ylabel('Quantidade vendida em reais.')
            plt.xlabel('Produtos')
            plt.show()
        if decisao3 == 2:
            grupoUnico = []
            grupoUnico.clear()

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from produtos;')
                    grupo = cursor.fetchall()
            except:
                print('Erro na consulta!!!')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from estatisticaVendido')
                    vendidoGrupo = cursor.fetchall()
            except:
                print('Erro na consulta!!!')

            for i in grupo:
                grupoUnico.append(i['nome'])

            #print(grupoUnico)
            # verificar se tem elementos repetidos e apagar caso encontre algum
            grupoUnico = sorted(set(grupoUnico))
            quantFinal = []
            quantFinal.clear()

            for h in range(0, len(grupoUnico)):
                quantUnitaria = 0
                for i in vendidoGrupo:
                    if grupoUnico[h] == i['nome']:
                        quantUnitaria += 1
                quantFinal.append(quantUnitaria)

            plt.plot(grupoUnico, quantFinal)
            plt.ylabel('Quantidade Unitária Vendida')
            plt.xlabel('Produtos')
            plt.show()

    elif estado == 2:
        decisao3 = int ( input ( 'Digite 1 para pesquisar por dinheiro, 2 para pesquisar por quantidade unitária' ) )
        if decisao3 == 1:

            for i in produtos:
                nomeProdutos.append ( i['grupo'] )

                valores = []
                valores.clear ()

                for h in range ( 0, len ( nomeProdutos ) ):
                    somaValor = -1
                    for i in vendido:
                        if i['grupo'] == nomeProdutos[h]:
                            somaValor += i['preco']
                    if somaValor == -1:
                        valores.append ( 0 )
                    elif somaValor >= 0:
                        valores.append ( somaValor + 1 )

            plt.plot ( nomeProdutos, valores )
            plt.ylabel ( 'Quantidade vendida em reais.' )
            plt.xlabel ( 'Produtos' )
            plt.show ()

        if decisao3 == 2:
            grupoUnico = []
            grupoUnico.clear()

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from produtos;')
                    grupo = cursor.fetchall()
            except:
                print('Erro na consulta!!!')

            try:
                with conexao.cursor() as cursor:
                    cursor.execute('select * from estatisticaVendido')
                    vendidoGrupo = cursor.fetchall()
            except:
                print('Erro na consulta!!!')

            for i in grupo:
                grupoUnico.append(i['grupo'])

            #print(grupoUnico)
            # verificar se tem elementos repetidos e apagar caso encontre algum
            grupoUnico = sorted(set(grupoUnico))
            quantFinal = []
            quantFinal.clear()

            for h in range(0, len(grupoUnico)):
                quantUnitaria = 0
                for i in vendidoGrupo:
                    if grupoUnico[h] == i['grupo']:
                        quantUnitaria += 1
                quantFinal.append(quantUnitaria)

            plt.plot(grupoUnico, quantFinal)
            plt.ylabel('Quantidade Unitária Vendida')
            plt.xlabel('Produtos')
            plt.show()


while not autentico:
    decisao = int(input('Digite 1 para Logar e 2 para se Cadastrar'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros;')
            resultado = cursor.fetchall()
    except:
        print('Erro ao conectar ao Banco de Dados')

    autentico, usuarioSupremo = logarCadastrar(decisao)

if autentico == True:
    print('autenticado...')

    if usuarioSupremo == True:
        decisaoUsuario = 1

        while decisaoUsuario != 0:
            decisaoUsuario = int ( input ( 'Digite 0 para sair, 1 para cadastrar produtos, 2 para listar produtos cadastrados, 3 listar Pedidos, 4 para visualizar as estatisticas') )

            if decisaoUsuario == 1:
                cadastrarProdutos()
            elif decisaoUsuario == 2:
                listarProdutos()

                delete = int(input('Digite 1 para excluir Produto, 2 para sair'))
                if delete == 1:
                    excluirProdutos()
                    print('Produto excluido com sucesso!!!')
            elif decisaoUsuario == 3:
                listarPedidos()
            elif decisaoUsuario == 4:
                gerarEstatistica()




