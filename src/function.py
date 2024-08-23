import pandas as pd
from utils import validar_csv

def avaliar_clientes_csv(caminho_arquivo, pontuacao_minima, receita_minima):

    df = validar_csv(caminho_arquivo)

    if df is None:
        print("Não é possível avaliar clientes devido a um arquivo inválido.")
        return

    df['adequado'] = (df['pontuacao_engajamento'] >= pontuacao_minima) & (df['receita_anual'] >= receita_minima)
    
    for index, row in df.iterrows():
        status = "Adequado" if row['adequado'] else "Não Adequado"
        print(f"Cliente: {row['nome']} - Status: {status}")

