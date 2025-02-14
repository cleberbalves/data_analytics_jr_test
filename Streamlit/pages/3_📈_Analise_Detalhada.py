import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Título da Página
st.title("📈 Análise Detalhada")

# Função para carregar dados com cache
@st.cache_data
def load_data():
    conn = sqlite3.connect(r"C:\Users\Usuário\Documents\Desafio\educacao_sp.db")
    escolas = pd.read_sql_query("SELECT DRE, CODESC, NOMES FROM escolas", conn)
    educandos = pd.read_sql_query("SELECT CODESC, QTDE, IDADE, SERIEV FROM educandos LIMIT 100000", conn)
    conn.close()
    return escolas, educandos

# Carregar dados
try:
    escolas, educandos = load_data()
    st.success("Dados carregados com sucesso!")
except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
    st.stop()

# Relação entre Idade e Série
st.header("Relação entre Idade e Série")
st.write("Aqui você pode explorar a relação entre a idade dos alunos e a série que estão cursando.")

# Filtros interativos
st.subheader("Filtros")
idade_min = st.slider("Idade Mínima", int(educandos['IDADE'].min()), int(educandos['IDADE'].max()), int(educandos['IDADE'].min()))
idade_max = st.slider("Idade Máxima", int(educandos['IDADE'].min()), int(educandos['IDADE'].max()), int(educandos['IDADE'].max()))

# Aplicar filtros
educandos_filtrados = educandos[(educandos['IDADE'] >= idade_min) & (educandos['IDADE'] <= idade_max)]

# Gráfico de Dispersão
st.subheader("Gráfico de Dispersão: Idade vs Série")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=educandos_filtrados, x='IDADE', y='SERIEV', hue='QTDE', size='QTDE', sizes=(50, 200), ax=ax)
ax.set_title('Relação entre Idade e Série')
ax.set_xlabel('Idade')
ax.set_ylabel('Série')
st.pyplot(fig)

# Histograma de Idade
st.subheader("Histograma: Distribuição de Idade")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data=educandos_filtrados, x='IDADE', bins=20, kde=True, ax=ax)
ax.set_title('Distribuição de Idade dos Alunos')
ax.set_xlabel('Idade')
ax.set_ylabel('Frequência')
st.pyplot(fig)