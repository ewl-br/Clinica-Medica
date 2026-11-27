def ler_nome(mensagem):
    while True:
        nome = input(mensagem).strip()
        if nome and all(
            caractere.isalpha() or caractere.isspace() or caractere in "-'"
            for caractere in nome
        ):
            return nome
        print("Nome inválido. por favor, informe um nome válido.")


def ler_telefone(mensagem):
    while True:
        telefone = input(mensagem).strip()
        if telefone.isdigit() and len(telefone) in (10, 11):
            return telefone
        print("Telefone inválido. Digite somente os 10 ou 11 números, incluindo o DDD.")


def ler_id(mensagem):
    while True:
        try:
            identificador = int(input(mensagem))
            if identificador > 0:
                return identificador
        except ValueError:
            pass
        print("ID inválido. Digite um número inteiro positivo.")


def ler_obrigatorio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Este campo é obrigatório.")


def ler_email(mensagem):
    while True:
        email = input(mensagem).strip()
        partes = email.split("@")
        if (
            len(partes) == 2
            and partes[0]
            and "." in partes[1]
            and not partes[1].startswith(".")
            and not partes[1].endswith(".")
        ):
            return email
        print("E-mail inválido. Informe um endereço no formato nome@dominio.com.")
from datetime import datetime


def ler_data(mensagem):
    while True:
        valor = input(mensagem).strip()
        try:
            return datetime.strptime(valor, "%d-%m-%Y").date()
        except ValueError:
            print("Data inválida. Digite no formato DD-MM-AAAA (ex: 28-11-2026).")