
def cadastrar_paciente(conexao):
    cursor = conexao.cursor()
    nome = input("Nome: ")
    data_nascimento =(input("Data de Nascimento: "))
    cpf = input("CPF: ")
    telefone =input("Telefone: ")    

    sql = """
    INSERT INTO paciente (nome, data_nascimento, cpf, telefone)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql, (nome, data_nascimento, cpf, telefone ))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Cadastro concluído")


def listar_paciente(conexao):
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM paciente")
    paciente = cursor.fetchall()
    if not paciente:
        print("Nenhum paciente cadastrado")
    else:
        for paciente in paciente:
            print(f"ID: {paciente[0]}")
            print(f"Nome: {paciente[1]}")
            print(f"Data de Nascimento: {paciente[2]}")
            print(f"CPF: {paciente[3]}")
            print(f"Telefone: {paciente[4]}")
    cursor.close()
    conexao.close()

def atualizar_paciente(conexao):
    cursor = conexao.cursor()
    id_paciente = int(input("ID do paciente: "))
    novo_nome = input("Digite novo nome: ")
    nova_data_nascimento = input("Digite a nova data de nascimento: ")
    novo_cpf = int(input("Digite o novo cpf: "))
    novo_telefone = int(input("Digite o novo telefone: "))

    sql = """
    UPDATE paciente
    SET nome = %s, data_nascimento = %s, cpf = %s, telefone = %s
    WHERE id = %s
    """
    cursor.execute(
        sql,
        (novo_nome, nova_data_nascimento, novo_cpf, novo_telefone, id_paciente),
    )
    atualizados = cursor.rowcount
    conexao.commit()
    cursor.close()
    conexao.close()

    if atualizados > 0:
        print("Paciente atualizado")
    else:
        print("Paciente não encontrado")

def excluir_paciente(conexao):
    cursor = conexao.cursor()
    id_paciente = int(input("ID do paciente: "))
    sql = "DELETE FROM paciente WHERE id = %s"
    cursor.execute(sql, (id_paciente,))
    excluidos = cursor.rowcount
    conexao.commit()
    cursor.close()
    conexao.close()
    if excluidos > 0:
        print("Paciente excluido")
    else:           
        print("Paciente não encontrado")