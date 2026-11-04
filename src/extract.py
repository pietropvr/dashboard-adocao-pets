import pandas as pd

# Define o caminho e carrega os dados brutos
caminho_arquivo = 'data/raw/animais.csv'
df = pd.read_csv(caminho_arquivo)

# Mostra um resumo das colunas carregadas
print("Dados carregados com sucesso!")
print(df.info())