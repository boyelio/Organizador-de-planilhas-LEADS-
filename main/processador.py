import pandas as pd

def carregar_planilha(caminho):
    if caminho.endswith(".xlsx") or caminho.endswith(".xls"):
        return pd.read_excel(caminho)
    elif caminho.endswith(".csv"):
        return pd.read_csv(caminho)
    else:
        raise ValueError("Formato de arquivo não suportado.")
    
def remover_colunas(df, colunas):
    df = df.drop(columns=colunas)
    return df

def salvar(df, caminho):
    df.to_excel(caminho, index=False)

def renomear_colunas(df, novo_nome):
    df = df.rename(columns=novo_nome)
    return df

def reorganizar_colunas(df, nova_ordem):
    df = df[nova_ordem]
    return df