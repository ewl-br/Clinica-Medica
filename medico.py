from validacoes import ler_email, ler_id, ler_nome, ler_obrigatorio, ler_telefone


def cadastrar_medico(conexao):
    cursor = conexao.cursor()
    nome = ler_nome("Nome do médico: ")
    crm = ler_obrigatorio("Digite o CRM: ")
    especialidade = ler_obrigatorio("Qual a especialidade: ")
    email = ler_email("Digite o e-mail: ")
    telefone = ler_telefone("Telefone (somente números com DDD): ")

    sql = """
    INSERT INTO medico (nome, crm, especialidade, email, telefone)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (nome, crm, especialidade, email, telefone))
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Médico cadastrado com sucesso.")


def listar_medico(conexao):
    cursor = conexao.cursor()
    cursor.execute(
        "SELECT id, nome, crm, especialidade, email, telefone FROM medico"
    )
    medicos = cursor.fetchall()
    if not medicos:
        print("Nenhum médico cadastrado.")
    else:
        for medico in medicos:
            print(f"ID: {medico[0]}")
            print(f"Nome: {medico[1]}")
            print(f"CRM: {medico[2]}")
            print(f"Especialidade: {medico[3]}")
            print(f"E-mail: {medico[4]}")
            print(f"Telefone: {medico[5]}")
    cursor.close()
    conexao.close()


def excluir_medico(conexao):
    cursor = conexao.cursor()
    id_medico = ler_id("Digite o ID do médico: ")
    cursor.execute("DELETE FROM medico WHERE id = %s", (id_medico,))
    excluidos = cursor.rowcount
    conexao.commit()
    cursor.close()
    conexao.close()
    if excluidos > 0:
        print("Médico excluído.")
    else:
        print("Médico não encontrado.")


def atualizar_medico(conexao):
    cursor = conexao.cursor()
    id_medico = ler_id("ID do médico: ")
    nome = ler_nome("Novo nome: ")
    crm = ler_obrigatorio("Novo CRM: ")
    especialidade = ler_obrigatorio("Nova especialidade: ")
    email = ler_email("Novo e-mail: ")
    telefone = ler_telefone("Novo telefone (somente números com DDD): ")

    sql = """
    UPDATE medico
    SET nome = %s, crm = %s, especialidade = %s, email = %s, telefone = %s
    WHERE id = %s
    """
    cursor.execute(sql, (nome, crm, especialidade, email, telefone, id_medico))
    atualizados = cursor.rowcount
    conexao.commit()
    cursor.close()
    conexao.close()
    if atualizados > 0:
        print("Médico atualizado.")
    else:
        print("Médico não encontrado.")
