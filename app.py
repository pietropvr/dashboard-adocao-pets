import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="Dashboard de Adoção PET", layout="wide")

# Título e descrição
st.title("Dinâmica de Adoção de Animais de Estimação")
st.write("Este painel analisa o desfecho dos animais num abrigo, permitindo explorar quais características influenciam a adoção.")

# Carregar os dados
@st.cache_data
def load_data():
    return pd.read_csv('data/processed/animais_processados.csv')

df = load_data()

# ==========================================
# 1. MENUS DE FILTROS (BARRA LATERAL)
# ==========================================
st.sidebar.header("Filtros")

especies = df['tipo_animal'].dropna().unique().tolist()
especie_selecionada = st.sidebar.selectbox("Selecione a Espécie:", ["Todas"] + especies)

sexos = df['sexo_desfecho'].dropna().unique().tolist()
sexo_selecionado = st.sidebar.selectbox("Selecione o Sexo:", ["Todos"] + sexos)

faixas = df['faixa_etaria'].dropna().unique().tolist()
faixa_selecionada = st.sidebar.selectbox("Selecione a Faixa Etária:", ["Todas"] + faixas)

racas = sorted(df['raca'].dropna().unique().tolist())
racas_selecionadas = st.sidebar.multiselect("Selecione a(s) Raça(s):", racas, placeholder="Escolha ou digite a raça")

# ==========================================
# 2. APLICAÇÃO DOS FILTROS (LÓGICA)
# ==========================================
# Começamos com a base completa
df_filtrado = df.copy()

# Vamos "afunilando" a base de acordo com as escolhas
if especie_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado['tipo_animal'] == especie_selecionada]

if sexo_selecionado != "Todos":
    df_filtrado = df_filtrado[df_filtrado['sexo_desfecho'] == sexo_selecionado]

if faixa_selecionada != "Todas":
    df_filtrado = df_filtrado[df_filtrado['faixa_etaria'] == faixa_selecionada]

if racas_selecionadas:
    df_filtrado = df_filtrado[df_filtrado['raca'].isin(racas_selecionadas)]


# ==========================================
# 3. MÉTRICAS E GRÁFICOS (VISUAL)
# ==========================================
st.subheader(f"Análise para: {especie_selecionada}")

# Cria cartões visuais superiores (KPIs)
col1, col2, col3 = st.columns(3)
total_registos = len(df_filtrado)
total_adocoes = len(df_filtrado[df_filtrado['tipo_desfecho'] == 'Adoção'])
taxa_adocao = (total_adocoes / total_registos) * 100 if total_registos > 0 else 0

col1.metric("Total de Registos", total_registos)
col2.metric("Total de Adoções", total_adocoes)
col3.metric("Taxa de Adoção", f"{taxa_adocao:.1f}%")

# Organiza o gráfico
st.write("### Volume por Tipo de Desfecho")
contagem_desfecho = df_filtrado['tipo_desfecho'].value_counts()
st.bar_chart(contagem_desfecho)