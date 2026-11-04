import pandas as pd

# 1. Carrega os dados brutos
df = pd.read_csv('data/raw/animais.csv')

# 2. Traduz as colunas
colunas_traduzidas = {
    'Animal ID': 'id_animal', 'Name': 'nome', 'DateTime': 'data_hora',
    'MonthYear': 'mes_ano', 'Date of Birth': 'data_nascimento',
    'Outcome Type': 'tipo_desfecho', 'Outcome Subtype': 'subtipo_desfecho',
    'Animal Type': 'tipo_animal', 'Sex upon Outcome': 'sexo_desfecho',
    'Age upon Outcome': 'idade_desfecho', 'Breed': 'raca', 'Color': 'cor'
}
df = df.rename(columns=colunas_traduzidas)

# 3. Limpeza e Tipos de Dados
df = df.dropna(subset=['tipo_desfecho'])
df['data_hora'] = pd.to_datetime(df['data_hora'], format='mixed')
df['data_nascimento'] = pd.to_datetime(df['data_nascimento'], format='mixed')

df = df.dropna(subset=['sexo_desfecho'])
traducao_sexo = {
    'Intact Female': 'Fêmea (Não-Castrada)', 'Spayed Female': 'Fêmea (Castrada)',
    'Intact Male': 'Macho (Não-Castrado)', 'Neutered Male': 'Macho (Castrado)',
    'Unknown': 'Desconhecido'
}
df['sexo_desfecho'] = df['sexo_desfecho'].replace(traducao_sexo)

# 4. Traduz os valores internos
traducao_animal = {'Dog': 'Cachorro', 'Cat': 'Gato', 'Bird': 'Pássaro', 'Other': 'Outro', 'Livestock': 'Gado'}
traducao_desfecho = {
    'Lost': 'Perdido', 'Stolen': 'Roubado',
    'Adoption': 'Adoção', 'Transfer': 'Transferência', 
    'Return to Owner': 'Devolvido ao Dono', 'Euthanasia': 'Eutanásia', 
    'Died': 'Óbito', 'Disposal': 'Descarte', 'Relocate': 'Realocado', 
    'Missing': 'Desaparecido', 'Rto-Adopt': 'Devolvido-Adotado'
}

df['tipo_animal'] = df['tipo_animal'].replace(traducao_animal)
df['tipo_desfecho'] = df['tipo_desfecho'].replace(traducao_desfecho)

# Calcula a idade exata em dias
df['idade_dias'] = (df['data_hora'] - df['data_nascimento']).dt.days

# Cria uma função para classificar a faixa etária
def categorizar_idade(dias):
    if pd.isna(dias) or dias < 0: return 'Desconhecido'
    if dias <= 365: return 'Filhote (Até 1 ano)'
    if dias <= 1095: return 'Jovem (1 a 3 anos)'
    if dias <= 2555: return 'Adulto (3 a 7 anos)'
    return 'Sênior (Mais de 7 anos)'

df['faixa_etaria'] = df['idade_dias'].apply(categorizar_idade)

# Traduz 'Mix' para 'SRD' (Sem Raça Definida) na coluna de raças
df['raca'] = df['raca'].astype(str).apply(lambda x: x.replace('Mix', 'SRD') if 'Mix' in x else x)

# 5. Guarda os dados processados
caminho_processado = 'data/processed/animais_processados.csv'
df.to_csv(caminho_processado, index=False)

print(f"Limpeza e tradução concluídas! Ficheiro guardado em: {caminho_processado}")