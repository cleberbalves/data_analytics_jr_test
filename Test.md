No repositório você encontrará dentro do diretório Data, em um arquivo compactado **Data.rar** os arquivos .csv disponibilizados como dataset, esses são os dados iniciais e **obrigatoriamente** devem estar na resolição do teste **mas não os únicos, fique a vontade** Boa sorte!


**Questão 1 - Utilize Python**

Como primeiro passo do desafio, faça a leitura/importação desses arquivos via python e realize o upload/carregamento desses dados em um banco **SQLite**.

- Crie um schema chamado: **test_analytics**
- Crie as tabelas com os mesmos nomes dos arquivos .csv
- Respeite a tipagem e os nomes das colunas dos arquivos .csv

***Dica***: Você pode utilizar o **sqlalchemy**

**Questão 2 - Utilize SQL**

Estabeleça uma relação entre as tabelas **escolas** e  **alunos** em uma nova tabela, chamada **‘escolas_alunos’**. Faça o mesmo para a dados externo se for utilizar.


**Questão 3 - Utilize SQL ou Python**

Faça uma análise exploratória dos dados no sentido de validar a qualidade dos dados destes datasets. Use sua criatividade e imaginação para buscar sujeiras na base de dados.

Lembre-se que queremos gerar insights com dados, então realize relações com tabelas que nos forneçam alguma informação relevante para os dados tratados analisados. Crie análises exploratórias dos dados.

***Dica***: Você pode utilizar o Jupyter notebook e compartilhar o passos a passo.

**Exemplos:** 

- Qual a proporção entre  alunos pela perspéctica dos perfis.
- Qual a densidade entre perfis e escola.
- Qual a proporção entre alunos e as regiões de São Paulo


**Questão 4 - Utilize SQL**

Encontre uma relação de dados entre as tabelas gerando mini datasets para analises mais especificas.

**Exemplo:**

Esquematize uma relação entre os **alunos** e **regiões** de São Paulo. 

***Dica***: A tabela escolas contem **cep**, **latitude** e **longitude**


**Questão 5 - Storytelling**

Nossa função exige que tenhamos a capacidade de repassar nossos insights com clareza na comunicação e profundo entendimento de negócio. Então monte uma apresentação de seus insights utilizando a ferramenta que mais se sentir confortável.

**Exemplos:** 

- Power Bi
- Tableau
- Looker Studio
- Colab

***Dica***: Você pode utilizar o Streamlit ou Plotly (**é o que mais utilizamos**)
