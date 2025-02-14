import streamlit as st
from PIL import Image

# Configuração da Página
st.set_page_config(page_title="🏠 Home - Análise Educacional Teste Cleber Brito Alves", layout="wide")

# Título com Estilo
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📊 Bem-vindo ao App de Análise Educacional</h1>", unsafe_allow_html=True)

# Imagem de Destaque
st.image(r"C:\Users\Usuário\Documents\Desafio\Streamlit\2741545-professor-explica-matematica-graficos-na-lousa-plana-ilustracao-processo-de-estudo-na-universidade-escola-aprendizagem-matematica-professor-e-aluno-isolado-persondns-de-desenhos-an.jpg", use_container_width=True) 



# Seção de Introdução
st.markdown("""
### 🎯 O que você encontrará aqui?
🔹 Visualização de dados interativos  
🔹 Comparação entre escolas e alunos  
🔹 Insights sobre desempenho educacional  
""")

# Criando Botões de Navegação
col1, col2 = st.columns(2)
with col1:
    if st.button("📊 Análise Geral"):
        st.switch_page("pages/2_📊_Analise_Geral.py")

with col2:
    if st.button("📈 Análise Detalhada"):
        st.switch_page("pages/3_📈_Analise_Detalhada.py")

# Rodapé
st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)
st.markdown("📢 **Dica:** Use o menu lateral para navegar entre as seções!")
