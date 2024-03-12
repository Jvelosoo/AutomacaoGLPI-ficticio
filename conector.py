import mysql.connector

def conectar_banco_de_dados():
    try:
        # Estabeleça a conexão com o banco de dados
        conexao = mysql.connector.connect(
            host="",
            port="",
            user="",
            password="",
            database=""
        )

        if conexao.is_connected():
            print("Conexão bem-sucedida!")
            return conexao

    except mysql.connector.Error as erro:
        print("Erro ao conectar ao banco de dados:", erro)
        return None

def fechar_conexao(conexao):
    if conexao.is_connected():
        conexao.close()
        print("Conexão fechada.")