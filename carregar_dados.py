import os
import pandas as pd
from sqlalchemy import create_engine

# Caminhos das subpastas
base_dir = r'C:\Users\Usuário\Documents\Desafio\data_analytics_jr_test\Data\Data\Data'
escolas_dir = os.path.join(base_dir, 'Escolas')
educandos_dir = os.path.join(base_dir, 'Perfil dos educandos')

# Conectar ao banco de dados SQLite
engine = create_engine('sqlite:///educacao_sp.db')
conn = engine.connect()

# Função para renomear colunas duplicadas
def rename_duplicate_columns(df):
    cols = pd.Series(df.columns)
    for dup in cols[cols.duplicated()].unique():
        cols[cols[cols == dup].index.values.tolist()] = [dup + '_' + str(i) if i != 0 else dup for i in range(sum(cols == dup))]
    df.columns = cols
    return df

# Função para carregar e tratar CSVs de uma pasta
def carregar_csvs_para_sqlite(pasta, nome_tabela):
    all_data = []
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.csv'):
            caminho_arquivo = os.path.join(pasta, arquivo)
            print(f"Carregando arquivo: {caminho_arquivo}")
            try:
                # Carregar o CSV com pandas e usar o delimitador correto
                df = pd.read_csv(caminho_arquivo, delimiter=';', encoding='latin1')
                # Normalizar os nomes das colunas
                df.columns = df.columns.str.strip().str.upper()
                # Renomear colunas duplicadas
                df = rename_duplicate_columns(df)
                all_data.append(df)
            except Exception as e:
                print(f"Erro ao carregar o arquivo {caminho_arquivo}: {e}")
    
    # Concatenar todos os DataFrames em um único DataFrame
    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        # Remover colunas duplicadas do DataFrame final
        final_df = final_df.loc[:, ~final_df.columns.duplicated()]
        # Verificar e renomear colunas duplicadas no DataFrame final
        final_df = rename_duplicate_columns(final_df)
        # Verificar colunas duplicadas antes de salvar
        print("Colunas duplicadas no DataFrame final:", final_df.columns[final_df.columns.duplicated()])
        # Salvar o DataFrame final no banco de dados SQLite
        final_df.to_sql(nome_tabela, conn, if_exists='replace', index=False)

# Carregar e tratar dados das escolas
carregar_csvs_para_sqlite(escolas_dir, 'escolas')

# Carregar e tratar dados dos educandos
carregar_csvs_para_sqlite(educandos_dir, 'educandos')

print("Dados carregados e tratados com sucesso!")
conn.close()