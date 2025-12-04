import pandas as pd
import re

def limpar_telefone(numero):
    """Limpa telefones e força padrão 55XXXXXXXXXXX"""
    
    if pd.isna(numero):
        return numero

    apenas_numeros = re.sub(r"\D", "", str(numero))

    if apenas_numeros.startswith("55"):
        return apenas_numeros
    
    if len(apenas_numeros) == 11:
        return "55" + apenas_numeros

    if len(apenas_numeros) == 9:
        return "55" + apenas_numeros

    return apenas_numeros

def limpar_coluna_telefone(df, coluna):
    df[coluna] = df[coluna].apply(limpar_telefone)
    return df

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

def analisar_colunas(df):
    analise = {}

    for coluna in df.columns:
        serie = df[coluna]

        info = {
            "tipo": str(serie.dtype),
            "valores_unicos": serie.nunique(),
            "valores_vazios": serie.isna().sum(),
            "exemplos": serie.dropna().unique()[:5].tolist()
        }

        # Se for numérico → adicionar estatísticas
        if pd.api.types.is_numeric_dtype(serie):
            info["minimo"] = serie.min()
            info["maximo"] = serie.max()
            info["media"] = serie.mean()

        # Se for texto → tamanho médio
        if pd.api.types.is_string_dtype(serie):
            info["tamanho_medio"] = serie.dropna().astype(str).str.len().mean()

        analise[coluna] = info

    return analise