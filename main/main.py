from processador import *
import pandas as pd
def menu():
    print("\n===== REORGANIZADOR DE LEADS =====\n")

    caminho = input("Digite o caminho da planilha (.xlsx ou .csv): ")

    df = carregar_planilha(caminho)
    print("\nColunas detectadas:")
    for col in df.columns:
        print(f"- {col}")
    df.columns = df.columns.str.strip()

    df = carregar_planilha(caminho)

    print("\n===== ANÁLISE DAS COLUNAS =====\n")
    analise = analisar_colunas(df)

    for coluna, dados in analise.items():
        print(f"📌 Coluna: {coluna}")
        print(f"- Tipo: {dados['tipo']}")
        print(f"- Valores únicos: {dados['valores_unicos']}")
        print(f"- Valores vazios: {dados['valores_vazios']}")
        print(f"- Exemplos: {dados['exemplos']}")

        if "minimo" in dados:
            print(f"- Min: {dados['minimo']}")
            print(f"- Máx: {dados['maximo']}")
            print(f"- Média: {dados['media']}")

        if "tamanho_medio" in dados:
            print(f"- Tamanho médio (texto): {dados['tamanho_medio']:.2f}")

        print()

    print("\nO que deseja fazer?")
    print("1 - Renomear colunas")
    print("2 - Reordenar colunas")
    print("3 - Remover colunas")
    print("4 - Exportar e sair")

    opcao = 10
    while opcao != 0:
        opcao = input("Escolha: ")

        if opcao == "1":
            novo_nome = {}
            print("\nDigite o novo nome das colunas (ou deixe vazio para manter):\n")
            print(df.columns.tolist())
            for col in df.columns:
                novo = input(f"{col} → ")
                if novo.strip() != "":
                    novo_nome[col] = novo
            df = renomear_colunas(df, novo_nome)

        elif opcao == "2":
            print("\nDigite a ordem desejada, separada por vírgulas:")
            print(df.columns.tolist())
            print("Exemplo: nome,email,telefone")
            ordem = input("→ ").split(",")
            df = reorganizar_colunas(df, ordem)

        elif opcao == "3":
            print("\nDigite as colunas que deseja remover, separadas por vírgula:")
            print(df.columns.tolist())
            rem = input("→ ").split(",")
            df = remover_colunas(df, rem)
        if opcao == 0:
            break

    caminho_saida = input("\nNome do arquivo final (ex: resultado.xlsx): ")
    salvar(df, caminho_saida)

    print("\nArquivo gerado com sucesso!")


if __name__ == "__main__":
    menu()