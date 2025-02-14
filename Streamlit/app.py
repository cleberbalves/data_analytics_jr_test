import streamlit as st
import plotly.express as px
from PIL import Image

# Configuração da Página
st.set_page_config(page_title="📊 Dashboard - Análise Educacional", layout="wide")

# Título com Estilo
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📊 Dashboard de Análise Educacional</h1>", unsafe_allow_html=True)

# Imagem de Destaque
st.image(r"C:\Users\Usuário\Documents\Desafio\Streamlit\29238048-ilustracaoial-grafico-personagem-de-desenho-animado-da-educacao-vetor.jpg", use_container_width=True)

# Seção de Destaques
st.markdown("## 🔍 Principais Indicadores")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="📚 Escolas Analisadas", value="250+", delta="↑ 5%")

with col2:
    st.metric(label="👩‍🎓 Alunos Cadastrados", value="12.000+", delta="↑ 8%")

with col3:
    st.metric(label="📈 Crescimento Anual", value="15%", delta="📊 +3% este ano")



# Seção de Insights
st.markdown("""
### 🏆 Destaques do Dashboard
✔️ Tendências de desempenho escolar  
✔️ Comparação entre escolas e turmas  
✔️ Insights para melhoria na educação  
""")

# Rodapé
st.markdown("<hr style='border:1px solid #ccc;'>", unsafe_allow_html=True)
st.markdown("📢 **Dica:** Use os gráficos interativos para explorar os dados em detalhes!")
