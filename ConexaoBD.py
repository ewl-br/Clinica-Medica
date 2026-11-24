import psycopg2
def conectar():     
    conexao=psycopg2.connect(
    host="localhost",
    database="clinica_medica",
    user="postgres",
    password="123456",
    port="5432",
)
    return conexao
        