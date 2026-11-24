def cadastrar_medico(conexao):
    cursor=conexao.cursor()
    nome=input("Nome do médico: ")
    CRM = input("Digite o CRM: ")
    especialidade=input("Qual a especialidade: ")
    email=input("Digite o email: ")

    sql= """" INSERT INTO medico (nome,CRM,especialidade,email)
    VALUES(%s,%s,%s,%s)
    """
    cursor.execute(sql,(nome,CRM,especialidade,email))
    cursor.commit()
    conexao.commit()
    conexao.close()
    print(" Médico Cadastrado com Sucesso")

def listar_medico(conexao):
    cursor=conexao.cursor()
    cursor.execute("SELECT * FROM medico")
    medico= cursor.fetchall()
    if not medico:
        print("Não encontrado ou não cadastrado") 
    else:
        for medico in medico:
            print(f"ID: {medico[0]}")
            print(f"Nome: {medico[1]}")
            print(f"CRM: {medico[2]}")
            print(f"especialidade: {medico[3]}")
            print(f"email: {medico[4]}")
    cursor.close()
    conexao.close()

def excluir_medico(conexao):
    cursor=conexao.cursor
    id_medico = int(input("Digite o ID do médico:"))
    sql = """ DELETE FROM medico WHERE id =%s
    """
    cursor.execute(sql,(id_medico))
    print("Médico excluido")
    excluido=cursor.rowcount
    conexao.commit
    cursor.close()
    conexao.close()
    if excluido > 0:
        print("Médico excluido")
    else:
        print("médico não encontrado") 

def atualizar_medico(conexao):
    cursor=conexao.cursor()
    