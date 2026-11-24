from ConexaoBD import conectar
from paciente import (cadastrar_paciente, atualizar_paciente, listar_paciente, excluir_paciente)


def menu():
    print("1 - Cadastrar paciente")
    print("2 - Atualizar paciente")
    print("3 - Listar pacientes")
    print("4 - Excluir paciente")
    print("5 - Sair")


def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        match opcao:
            case "1":
                cadastrar_paciente(conectar())
            case "2":
                atualizar_paciente(conectar())
            case "3":
                listar_paciente(conectar())
            case "4":
                excluir_paciente(conectar())    
            case "5":
                print("Encerrando...")
                break
            case _:
                print("Opção inválida")
    print("1 - Cadastrar paciente")


if __name__ == "__main__":
    main()  
