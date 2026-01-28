## Bônus – Definição e Implementação de um Common Data Model (CDM)

Como parte do bônus do Item 4, foi definido e implementado um **Common Data Model (CDM)** para padronizar semanticamente os dados utilizados ao longo do projeto, seguindo os princípios do **Microsoft Common Data Model (CDM)**.

O objetivo do CDM é desacoplar a estrutura física da fonte de dados do consumo analítico, garantindo consistência semântica, governança e reutilização das regras de qualidade de dados, independentemente da origem (CSV local, PostgreSQL ou pipelines da Dadosfera).

---

### Estratégia adotada

A implementação do CDM seguiu as seguintes diretrizes:

- Modelo orientado a eventos (viagens de mobilidade)
- Padronização de nomes de colunas e tipos de dados
- Criação de colunas derivadas com significado de negócio
- Anonimização de identificadores sensíveis
- Preservação da tabela original de ingestão (RAW)

Para **não impactar fluxos já existentes**, foi criada uma **cópia da tabela original diretamente no Supabase**, permitindo testes e validações independentes do modelo canônico.

---

### Implementação no PostgreSQL (Supabase)

O CDM foi implementado no PostgreSQL (Supabase) por meio da criação de uma **nova tabela física**, derivada da tabela original de ingestão:

- **Tabela original (RAW):**  
  `nyc_taxi_trips_2024_01`

- **Tabela CDM (canônica):**  
  `nyc_taxi_trips_2024_01_cdm`

A criação da tabela CDM foi realizada a partir de uma query SQL que aplica as transformações semânticas necessárias (padronização, colunas derivadas e anonimização), mantendo a tabela RAW intacta.

A query utilizada para essa criação está documentada no arquivo:

- **`create_nyc_taxi_trips_2024_01_cdm.sql`**

Essa abordagem garante rastreabilidade, rollback seguro e comparação direta entre as camadas RAW e CDM.

---

### Entidade canônica: `mobility_trip`

A tabela `nyc_taxi_trips_2024_01_cdm` representa a entidade canônica **mobility_trip**, que descreve uma viagem individual.

Campos principais do modelo:

| Campo CDM | Descrição |
|----------|----------|
| vendor_id | Identificador anonimizado do provedor |
| pickup_datetime | Data/hora de início da viagem |
| dropoff_datetime | Data/hora de término da viagem |
| trip_duration_seconds | Duração da viagem em segundos |
| passenger_count | Número de passageiros |
| trip_distance_miles | Distância percorrida |
| pickup_location_id | Local de embarque |
| dropoff_location_id | Local de desembarque |
| payment_type | Tipo de pagamento |
| fare_amount | Valor base da corrida |
| total_amount | Valor total pago |

---

### Qualidade de dados aplicada sobre o CDM

Após a criação da tabela CDM, a validação de qualidade passou a ser executada diretamente sobre o modelo canônico, utilizando **Great Expectations com a API Validator**.

O processo de validação está implementado no script:

- **`data_quality_postgresql_cdm.py`**

Esse script aplica o **mesmo conjunto de 22 regras de qualidade** utilizado na validação do dataset RAW, organizadas por:

- Completude  
- Validade  
- Domínio  
- Consistência temporal  

Ao final da execução, é gerado automaticamente um relatório textual contendo o status da validação e o detalhamento das regras com falha:

- **`data_quality_report_postgres_cdm.txt`**

---

### Comparação entre camadas RAW e CDM

A separação entre as camadas RAW e CDM permite:

- Comparar a qualidade dos dados antes e depois da modelagem semântica
- Avaliar o impacto positivo do CDM na consistência e interpretabilidade dos dados
- Reutilizar as mesmas regras de qualidade em diferentes camadas do pipeline

Essa abordagem reforça o conceito de **qualidade de dados orientada a contrato**, em que as validações são aplicadas sobre o modelo canônico, e não sobre estruturas físicas específicas da fonte.

---

### Benefícios da adoção do CDM no projeto

A implementação do Common Data Model trouxe os seguintes benefícios:

- Independência da fonte de dados
- Reutilização das regras de qualidade
- Redução de acoplamento entre ingestão e consumo
- Base preparada para análises avançadas e modelos de IA
- Governança explícita e auditável
- Evolução segura do pipeline sem quebra de dependências

O CDM passa a atuar como **ponto único de verdade analítica**, alinhando ingestão, qualidade, exploração e consumo de dados.

---

### Referência

- Microsoft Common Data Model  
  https://learn.microsoft.com/en-us/common-data-model/
