import sqlite3

# Nome do banco de dados ao qual o script se conectará
nome_do_banco_de_dados = 'banco_de_dados_exemplo.db'

# Conectando ao banco de dados SQLite existente
conn = sqlite3.connect(nome_do_banco_de_dados)

# Criando um objeto cursor para executar comandos SQL
cursor = conn.cursor()

# Função para listar todos os usuários
def listar_usuarios():
    # Executando um comando SQL para selecionar todos os registros da tabela 'usuarios'
    cursor.execute('SELECT * FROM usuarios')

    # Obtendo todos os resultados da consulta
    usuarios = cursor.fetchall()

    # Imprimindo cada usuário
    for usuario in usuarios:
        print(usuario)

# Chamando a função para listar os usuários
listar_usuarios()

# Fechando a conexão com o banco de dados
conn.close()
