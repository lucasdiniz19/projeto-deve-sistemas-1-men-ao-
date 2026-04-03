import pymysql

try:
    conexao = pymysql.connect(
        host="localhost",
        user="root",
        password="61bfaculdade",
        database="financeiro_db", # O banco de dados foi criado mas não esta preenchido.
        port=3306
    )
    
    print("Conexão com o MySQL realizada com sucesso!")

    conexao.close()

except Exception as erro:
    print("Erro ao conectar no banco:")
    print(erro)
