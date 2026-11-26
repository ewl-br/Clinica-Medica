import psycopg2

from ConexaoBD import conectar
from medico import cadastrar_medico, atualizar_medico, listar_medico, excluir_medico
from paciente import cadastrar_paciente, atualizar_paciente, listar_paciente, excluir_paciente


def menu():
    print("1 - Cadastrar paciente")
    print("2 - Atualizar paciente")
    print("3 - Listar pacientes")
    print("4 - Excluir paciente")
    print("5 - Cadastrar médico")
    print("6 - Atualizar médico")
    print("7 - Listar médicos")
    print("8 - Excluir médico")
    print("9 - Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        operacoes = {
            "1": cadastrar_paciente,
            "2": atualizar_paciente,
            "3": listar_paciente,
            "4": excluir_paciente,
            "5": cadastrar_medico,
            "6": atualizar_medico,
            "7": listar_medico,
            "8": excluir_medico,
        }

        if opcao == "9":
            print("Encerrando...")
            break
        operacao = operacoes.get(opcao)
        if operacao is None:
            print("Opção inválida. Escolha uma opção de 1 a 9.")
            continue

        try:
            operacao(conectar())
        except psycopg2.Error as erro:
            print(f"Erro ao acessar o banco de dados: {erro}")


if __name__ == "__main__":
    main()