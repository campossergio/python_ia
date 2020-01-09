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

def logarCadastrar():
    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False

    if decisao == 1:
        nome = input('Digite seu Nome: ')
        senha = input('Digite sua Senha: ')

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
            else:
                autenticado = False

        if not autenticado:
            print('email ou senha errados')

    elif decisao == 2:
        print('Faça seu cadastro')
        nome = input('Digite seu Nome: ')
        senha = input('Digite sua Senha')

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



while not autentico:
    decisao = int(input('Digite 1 para Logar e 2 para se Cadastrar'))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros;')
            resultado = cursor.fetchall()
    except:
        print('Erro ao conectar ao Banco de Dados')

    autentico, usuarioSupremo = logarCadastrar()

if autentico == True:
    print('autenticado...')
