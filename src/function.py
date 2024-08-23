import pandas as pd

def avaliar_clientes_csv(caminho_arquivo, pontuacao_minima, receita_minima):

    df = pd.read_csv(caminho_arquivo)
    
    if not all(col in df.columns for col in ['nome', 'pontuacao_engajamento', 'receita_anual']):
        raise ValueError("O arquivo CSV deve conter as colunas 'nome', 'pontuacao_engajamento', e 'receita_anual'")
    
    df['adequado'] = (df['pontuacao_engajamento'] >= pontuacao_minima) & (df['receita_anual'] >= receita_minima)
    
    for index, row in df.iterrows():
        status = "Adequado" if row['adequado'] else "Não Adequado"
        print(f"Cliente: {row['nome']} - Status: {status}")

    avaliar_clientes_csv('./files/clientes.csv', pontuacao_minima=70, receita_minima=50000)
    