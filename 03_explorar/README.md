# Item 3 – Exploração e Catalogação dos Dados

Nesta etapa, o dataset foi explorado e catalogado na plataforma Dadosfera, seguindo boas práticas de organização de um Data Lake e governança de dados.

## Organização do Data Lake

Os dados foram inicialmente carregados em sua forma bruta (camada Landing/Raw) por meio da importação manual de arquivos. Após a ingestão, o dataset foi padronizado e disponibilizado no Catálogo de Dados (camada Standardized), ficando apto para exploração analítica e consumo por ferramentas de análise (camada Curated).

## Catalogação do Dataset

O dataset foi devidamente catalogado com nome, descrição e tags, facilitando sua descoberta e reutilização. Também foram adicionadas descrições para os principais campos, compondo um Dicionário de Dados que permite melhor entendimento do significado e uso das informações.

<img src="tags.png" alt="tags" width="400"/>

<img src="dataset_tabelas.png" alt="dataset_tabelas" width="400"/>

## Dicionário de Dados

Foram documentadas as colunas mais relevantes do dataset, incluindo campos temporais, geográficos e financeiros, garantindo clareza sobre a granularidade dos dados e seus possíveis usos analíticos.

| Coluna | Tipo | Descrição |
|------|------|-----------|
| VendorID | Integer | Identificador do provedor do serviço |
| tpep_pickup_datetime | Timestamp | Data e hora de início da viagem |
| tpep_dropoff_datetime | Timestamp | Data e hora de término da viagem |
| passenger_count | Integer | Número de passageiros |
| trip_distance | Float | Distância percorrida (milhas) |
| PULocationID | Integer | Zona de origem |
| DOLocationID | Integer | Zona de destino |
| payment_type | Integer | Tipo de pagamento |
| fare_amount | Float | Valor base da tarifa |
| tip_amount | Float | Valor da gorjeta |
| total_amount | Float | Valor total da viagem |

Essa etapa prepara o dataset para análises descritivas, visualizações e modelagens que serão realizadas nas fases seguintes do projeto.

## Bônus – Catalogação via API

A Dadosfera disponibiliza APIs para automação da catalogação de ativos, permitindo integração com pipelines e processos automatizados de governança.

Neste projeto, a catalogação foi realizada via interface da plataforma. Em um cenário produtivo, essa etapa poderia ser automatizada via API para atualização de descrições, tags e metadados de forma programática.
