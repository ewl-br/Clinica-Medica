import psycopg2

from ConexaoBD import conectar
from medico import cadastrar_medico, atualizar_medico, listar_medico, excluir_medico
from paciente import cadastrar_paciente, atualizar_paciente, listar_paciente, excluir_paciente
from consultas import cadastrar_consultas, atualizar_consultas, listar_consultas, excluir_consultas


def menu():
    """Exibe o menu principal do sistema no terminal."""
    print("\n" + "=" * 42)
    print("       SISTEMA DE GESTÃO DA CLÍNICA")
    print("=" * 42)
    print("\nPACIENTES")
    print("  1 - Cadastrar paciente")
    print("  2 - Atualizar paciente")
    print("  3 - Listar pacientes")
    print("  4 - Excluir paciente")
    print("\nMÉDICOS")
    print("  5 - Cadastrar médico")
    print("  6 - Atualizar médico")
    print("  7 - Listar médicos")
    print("  8 - Excluir médico")
    print("\nCONSULTAS")
    print("  9 - Cadastrar consulta")
    print(" 10 - Atualizar consulta")
    print(" 11 - Listar consultas")
    print(" 12 - Excluir consulta")
    print("\n 13 - Sair")
    print("=" * 42)


def preparar_banco():
    """Garante que a coluna motivo_consulta exista na tabela consultas."""
    conexao = conectar()
    try:
        with conexao.cursor() as cursor:
            cursor.execute(
                "ALTER TABLE consultas ADD COLUMN IF NOT EXISTS motivo_consulta TEXT"
            )
        conexao.commit()
    except psycopg2.Error:
        conexao.rollback()
        raise
    finally:
        conexao.close()


def main():
    """Controla o fluxo principal e o roteamento das opções do menu."""
    try:
        preparar_banco()
    except psycopg2.Error as erro:
        print(f"Aviso ao verificar estrutura da tabela consultas: {erro}")

    operacoes = {
        "1": cadastrar_paciente,
        "2": atualizar_paciente,
        "3": listar_paciente,
        "4": excluir_paciente,
        "5": cadastrar_medico,
        "6": atualizar_medico,
        "7": listar_medico,
        "8": excluir_medico,
        "9": cadastrar_consultas,
        "10": atualizar_consultas,
        "11": listar_consultas,
        "12": excluir_consultas,
    }

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "13":
            print("Encerrando...")
            break

        operacao = operacoes.get(opcao)
        if operacao is None:
            print("Opção inválida. Escolha uma opção de 1 a 13.")
            continue

        try:
            operacao(conectar())
        except psycopg2.Error as erro:
            print(f"Erro ao acessar o banco de dados: {erro}")


if __name__ == "__main__":
    main()