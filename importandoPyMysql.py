import pymysql.cursors

''' CONECTANDO COM O BANCO DE DADOS '''
''' PRECISA PASSAR ALGUNS PARAMETROS '''
conexao = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    db = 'cursopython',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor
)

'''
cursor = conexao.cursor()

x = 'drop table cursos'

cursor.execute(x)
#cursor.execute('create table cursos(nome varchar(50), idade int, curso varchar(30));')


# FECHANDO O BANCO DE DADOS
cursor.close()
conexao.close()
'''

''' FORMA MAIS PRATICA DE SE CONECTAR COM O BD '''

# CRIANDO TABELAS
#x = 'create table teste(nome varchar(30));'
#x = 'create table cursos ( id int primary key auto_increment, nome varchar(30) not null, curso varchar(30) not null);'
# EXCLUINDO TABELAS
#x = 'drop table teste;'

# INSERINDO DADOS EM UMA TABELA
#y = 'insert into teste values("Miguel Campos");'
#y = input('Digite seu nome: ')
#z = input('Digite seu curso: ')
# APÓS A INSERÇÃO DAR UM COMMIT

'''
with conexao.cursor() as cursor:
    cursor.execute('insert into cursos(nome, curso) values("{}", "{}")'.format(y, z))
    conexao.commit()

print('código executado com sucesso...')
'''

''' ACESSANDO OS DADOS QUE ESTÃO NO BD '''
with conexao.cursor() as cursor:
    cursor.execute('select * from cursos')
    resultado = cursor.fetchall()

for dados in resultado:
    print(dados)

# MOSTRAR APENAS OS NOMES OU OUTRO COLUNA ESPECÍFICA
for dado in resultado:
    print(dado['nome'])

for dado in resultado:
    print('O aluno(a) {} está fazendo o curso de {}'.format(dado['nome'], dado['curso']))

#print(dados)
print('código executado com sucesso!!!')
