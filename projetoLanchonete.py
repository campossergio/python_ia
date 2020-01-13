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
            decisaoUsuario = int ( input ( 'Digite 0 para sair, 1 para cadastrar produtos, 2 para listar produtos cadastrados' ) )

            if decisaoUsuario == 1:
                cadastrarProdutos()
            elif decisaoUsuario == 2:
                listarProdutos()

