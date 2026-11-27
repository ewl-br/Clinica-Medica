from validacoes import ler_data, ler_id, ler_obrigatorio


def cadastrar_consultas(conexao):
    """Cadastra uma nova consulta vinculando paciente, médico, data e motivo."""
    try:
        id_paciente = ler_id("ID do paciente: ")
        id_medico = ler_id("ID do médico: ")
        data_consulta = ler_data("Data da consulta (DD-MM-AAAA): ")
        motivo_consulta = ler_obrigatorio("Motivo da consulta: ")

        sql = """
        INSERT INTO consultas (id_paciente, id_medico, data_consulta, motivo_consulta)
        VALUES (%s, %s, %s, %s)
        """
        with conexao.cursor() as cursor:
            cursor.execute(
                sql,
                (id_paciente, id_medico, data_consulta, motivo_consulta),
            )
        conexao.commit()
        print("Consulta cadastrada com sucesso.")
    finally:
        conexao.close()


def listar_consultas(conexao):
    """Lista todas as consultas cadastradas com os nomes do médico e do paciente."""
    try:
        sql = """
        SELECT
            c.id_consulta,
            c.id_medico,
            m.nome AS nome_medico,
            c.id_paciente,
            p.nome AS nome_paciente,
            c.data_consulta,
            c.motivo_consulta
        FROM consultas c
        LEFT JOIN medicos m ON c.id_medico = m.id_medico
        LEFT JOIN pacientes p ON c.id_paciente = p.id_paciente
        ORDER BY c.data_consulta
        """
        with conexao.cursor() as cursor:
            cursor.execute(sql)
            consultas = cursor.fetchall()

        if not consultas:
            print("Nenhuma consulta cadastrada.")
            return

        print("\n" + "=" * 42)
        print("           LISTA DE CONSULTAS")
        print("=" * 42)
        for consulta in consultas:
            id_consulta = consulta[0]
            id_medico = consulta[1]
            nome_medico = consulta[2] or "Médico não encontrado"
            id_paciente = consulta[3]
            nome_paciente = consulta[4] or "Paciente não encontrado"
            data_formatada = consulta[5].strftime("%d-%m-%Y")
            motivo = consulta[6] or "Não informado"

            print(f"ID da consulta: {id_consulta}")
            print(f"Médico: {nome_medico} (ID: {id_medico})")
            print(f"Paciente: {nome_paciente} (ID: {id_paciente})")
            print(f"Data da consulta: {data_formatada}")
            print(f"Motivo da consulta: {motivo}")
            print("-" * 42)
    finally:
        conexao.close()


def atualizar_consultas(conexao):
    """Verifica se a consulta existe no banco e atualiza seus dados."""
    try:
        id_consulta = ler_id("ID da consulta: ")

        with conexao.cursor() as cursor:
            cursor.execute(
                "SELECT id_consulta FROM consultas WHERE id_consulta = %s",
                (id_consulta,),
            )
            if cursor.fetchone() is None:
                print("Consulta não encontrada.")
                return

            id_paciente = ler_id("Novo ID do paciente: ")
            id_medico = ler_id("Novo ID do médico: ")
            data_consulta = ler_data("Nova data (DD-MM-AAAA): ")
            motivo_consulta = ler_obrigatorio("Novo motivo da consulta: ")

            sql = """
            UPDATE consultas
            SET id_paciente = %s,
                id_medico = %s,
                data_consulta = %s,
                motivo_consulta = %s
            WHERE id_consulta = %s
            """
            cursor.execute(
                sql,
                (
                    id_paciente,
                    id_medico,
                    data_consulta,
                    motivo_consulta,
                    id_consulta,
                ),
            )
        conexao.commit()
        print("Consulta atualizada com sucesso.")
    finally:
        conexao.close()


def excluir_consultas(conexao):
    """Remove uma consulta do banco de dados a partir do seu ID."""
    try:
        id_consulta = ler_id("ID da consulta: ")
        with conexao.cursor() as cursor:
            cursor.execute(
                "DELETE FROM consultas WHERE id_consulta = %s",
                (id_consulta,),
            )
            excluidas = cursor.rowcount
        conexao.commit()

        if excluidas > 0:
            print("Consulta excluída com sucesso.")
        else:
            print("Consulta não encontrada.")
    finally:
        conexao.close()