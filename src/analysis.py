import pandas as pd
import matplotlib.pyplot as plt

# 1. Carrega os dados limpos
df = pd.read_csv('data/processed/animais_processados.csv')

# 2. Estatística Descritiva
print("--- Contagem de Animais por Espécie ---")
contagem_especie = df['tipo_animal'].value_counts()
print(contagem_especie)

# 3. Criação do Gráfico
plt.figure(figsize=(8, 5))
contagem_especie.plot(kind='bar', color=['#4C72B0', '#DD8452', '#55A868', '#C44E52', '#8172B3'])
plt.title('Quantidade Total de Animais por Espécie no Abrigo')
plt.xlabel('Espécie (Tipo de Animal)')
plt.ylabel('Quantidade de Registos')
plt.xticks(rotation=0)

# 4. Guarda o gráfico na pasta outputs
caminho_grafico = 'outputs/animais_por_especie.png'
plt.tight_layout()
plt.savefig(caminho_grafico)

print(f"\nSucesso! O gráfico foi guardado em: {caminho_grafico}")