from processador import *
import pandas as pd

def menu():
    print("\n===== REORGANIZADOR DE LEADS =====\n")

    caminho = input("Digite o caminho da planilha (.xlsx ou .csv): ")

    df = carregar_planilha(caminho)
    print("\nColunas detectadas:")
    for col in df.columns:
        print(f"- {col}")

    print("\nO que deseja fazer?")
    print("1 - Renomear colunas")
    print("2 - Reordenar colunas")
    print("3 - Remover colunas")
    print("4 - Exportar e sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        novo_nome = {}
        print("\nDigite o novo nome das colunas (ou deixe vazio para manter):\n")
        for col in df.columns:
            novo = input(f"{col} → ")
            if novo.strip() != "":
                novo_nome[col] = novo
        df = renomear_colunas(df, novo_nome)

    elif opcao == "2":
        print("\nDigite a ordem desejada, separada por vírgulas:")
        print("Exemplo: nome,email,telefone")
        ordem = input("→ ").split(",")
        df = reorganizar_colunas(df, ordem)

    elif opcao == "3":
        print("\nDigite as colunas que deseja remover, separadas por vírgula:")
        rem = input("→ ").split(",")
        df = remover_colunas(df, rem)

    caminho_saida = input("\nNome do arquivo final (ex: resultado.xlsx): ")
    salvar(df, caminho_saida)

    print("\nArquivo gerado com sucesso!")


if __name__ == "__main__":
    menu()