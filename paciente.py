
from validacoes import ler_id, ler_nome, ler_telefone


def cadastrar_paciente(conexao):
    cursor = conexao.cursor()
    nome = ler_nome("Nome: ")
    data_nascimento =(input("Data de Nascimento: "))
    cpf = input("CPF: ")
    telefone = ler_telefone("Telefone (somente números com DDD): ")

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
    id_paciente = ler_id("ID do paciente: ")
    novo_nome = ler_nome("Digite novo nome: ")
    nova_data_nascimento = input("Digite a nova data de nascimento: ")
    novo_cpf = input("Digite o novo CPF: ")
    novo_telefone = ler_telefone("Digite o novo telefone (somente números com DDD): ")

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
    id_paciente = ler_id("ID do paciente: ")
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