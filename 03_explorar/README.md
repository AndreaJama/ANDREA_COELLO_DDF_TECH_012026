# Item 3 – Exploração e Catalogação dos Dados

Nesta etapa, o dataset foi explorado e catalogado na plataforma Dadosfera, seguindo boas práticas de organização de um Data Lake e governança de dados.

## Organização do Data Lake

Os dados foram inicialmente carregados em sua forma bruta (camada Landing/Raw) por meio da importação manual de arquivos. Após a ingestão, o dataset foi padronizado e disponibilizado no Catálogo de Dados (camada Standardized), ficando apto para exploração analítica e consumo por ferramentas de análise (camada Curated).

## Catalogação do Dataset

O dataset foi devidamente catalogado com nome, descrição e tags, facilitando sua descoberta e reutilização. Também foram adicionadas descrições para os principais campos, compondo um Dicionário de Dados que permite melhor entendimento do significado e uso das informações.

## Dicionário de Dados

Foram documentadas as colunas mais relevantes do dataset, incluindo campos temporais, geográficos e financeiros, garantindo clareza sobre a granularidade dos dados e seus possíveis usos analíticos.

Essa etapa prepara o dataset para análises descritivas, visualizações e modelagens que serão realizadas nas fases seguintes do projeto.

## Bônus – Catalogação via API

A Dadosfera disponibiliza APIs para automação da catalogação de ativos, permitindo integração com pipelines e processos automatizados de governança.

Neste projeto, a catalogação foi realizada via interface da plataforma. Em um cenário produtivo, essa etapa poderia ser automatizada via API para atualização de descrições, tags e metadados de forma programática.
