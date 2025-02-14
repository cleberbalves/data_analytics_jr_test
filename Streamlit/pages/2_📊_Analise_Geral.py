import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração da Página
st.set_page_config(page_title="📊 Análise Geral", layout="wide")

# Título da Página
st.title("📊 Análise Geral")

# Função para carregar dados com cache
@st.cache_data
def load_data():
    conn = sqlite3.connect(r"C:\Users\Usuário\Documents\Desafio\educacao_sp.db")
    escolas = pd.read_sql_query("SELECT DRE, CODESC, NOMES, LATITUDE, LONGITUDE FROM escolas", conn)
    educandos = pd.read_sql_query("SELECT CODESC, QTDE, IDADE, SERIEV, SEXO, RACA, NEE FROM educandos LIMIT 100000", conn)
    conn.close()
    return escolas, educandos

# Carregar dados
try:
    escolas, educandos = load_data()
    st.success("✅ Dados carregados com sucesso!")
except Exception as e:
    st.error(f"❌ Erro ao carregar os dados: {e}")
    st.stop()

# Visualização das Tabelas
st.header("📋 Visualização das Tabelas")
st.write("Aqui estão as primeiras linhas das tabelas:")

st.write("**📚 Tabela Escolas:**")
st.dataframe(escolas.head())

st.write("**👨‍🎓 Tabela Educandos:**")
st.dataframe(educandos.head())

# Quantidade de Alunos por Escola
st.header("🏫 Quantidade de Alunos por Escola")
alunos_por_escola = educandos.groupby('CODESC')['QTDE'].sum().reset_index()
alunos_por_escola = alunos_por_escola.merge(escolas[['CODESC', 'NOMES']], on='CODESC', how='left')

# Gráfico de Barras Ajustado
st.write("📌 Top 10 escolas com mais alunos:")
top_escolas = alunos_por_escola.sort_values(by='QTDE', ascending=False).head(10)

fig, ax = plt.subplots(figsize=(8, 4))  # Reduzindo tamanho do gráfico
sns.barplot(
    data=top_escolas, 
    x='NOMES', 
    y='QTDE', 
    hue='NOMES',  # Ajuste para evitar o warning
    dodge=False,  # Evita barras deslocadas
    legend=False,  # Remove legenda desnecessária
    palette="pastel",
    ax=ax
)

ax.set_title("Top 10 Escolas com Mais Alunos", fontsize=12)
ax.set_xlabel("Escolas", fontsize=10)
ax.set_ylabel("Quantidade de Alunos", fontsize=10)
ax.tick_params(axis='x', rotation=45)  # Rotaciona os nomes para melhor visualização
st.pyplot(fig)

# Distribuição de Alunos por Sexo
st.header("⚧️ Distribuição de Alunos por Sexo")
distribuicao_sexo = educandos.groupby('SEXO')['QTDE'].sum().reset_index()

fig, ax = plt.subplots(figsize=(5, 5))  # Reduzindo tamanho
wedges, texts, autotexts = ax.pie(
    distribuicao_sexo['QTDE'], 
    labels=distribuicao_sexo['SEXO'], 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
)
ax.set_title('Distribuição de Alunos por Sexo')
st.pyplot(fig)

# Distribuição de Alunos por Raça
st.header("🎭 Distribuição de Alunos por Raça")
distribuicao_raca = educandos.groupby('RACA')['QTDE'].sum().reset_index()

fig, ax = plt.subplots(figsize=(8, 4))  # Reduzindo tamanho do gráfico
sns.barplot(data=distribuicao_raca, x='RACA', y='QTDE', hue="RACA", legend=False, palette="pastel", ax=ax)
ax.set_title('Distribuição de Alunos por Raça', fontsize=12)
ax.set_xlabel('Raça', fontsize=10)
ax.set_ylabel('Quantidade de Alunos', fontsize=10)
st.pyplot(fig)

# Distribuição de Alunos por Necessidade Especial
st.header("♿ Distribuição de Alunos por Necessidade Especial")
distribuicao_nee = educandos.groupby('NEE')['QTDE'].sum().reset_index()

fig, ax = plt.subplots(figsize=(5, 5))  # Reduzindo tamanho do gráfico
wedges, texts, autotexts = ax.pie(
    distribuicao_nee['QTDE'], 
    labels=distribuicao_nee['NEE'], 
    autopct='%1.1f%%', 
    startangle=90, 
    colors=['#ff9999', '#66b3ff']
)

ax.set_title('Distribuição de Alunos por Necessidade Especial')

# Ajustando a posição da legenda para fora do gráfico
ax.legend(wedges, distribuicao_nee['NEE'], title="NEE", loc="center left", bbox_to_anchor=(1, 0.5))

st.pyplot(fig)

# Mapa de Localização das Escolas
st.header("🗺️ Mapa de Localização das Escolas")
st.write("📍 Aqui está a localização das escolas no mapa.")

# Verifica se há dados de latitude e longitude
if 'LATITUDE' in escolas.columns and 'LONGITUDE' in escolas.columns:
    escolas['LATITUDE'] = pd.to_numeric(escolas['LATITUDE'], errors='coerce')
    escolas['LONGITUDE'] = pd.to_numeric(escolas['LONGITUDE'], errors='coerce')
    
    # Remove linhas com valores nulos
    escolas = escolas.dropna(subset=['LATITUDE', 'LONGITUDE'])
    
    # Exibe o mapa
    st.map(escolas[['LATITUDE', 'LONGITUDE']])
else:
    st.warning("⚠️ Dados de latitude e longitude não encontrados na tabela de escolas.")

