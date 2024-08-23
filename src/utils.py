import pandas as pd

def validar_csv(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo)
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return None
    
    colunas_necessarias = ['nome', 'pontuacao_engajamento', 'receita_anual']
    if not all(col in df.columns for col in colunas_necessarias):
        print(f"O arquivo CSV deve conter as colunas {colunas_necessarias}.")
        return None
    
    return df