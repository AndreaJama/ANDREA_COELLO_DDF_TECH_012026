## Item 6 – Modelagem de Dados

### Objetivo
Propor uma modelagem de dados analítica condizente com o cenário do cliente (e-commerce/logística), considerando os dados integrados nas etapas anteriores, com foco em eficiência analítica, visualização e geração de valor para o negócio.

---

## 6.1 Escolha da Abordagem de Modelagem

A modelagem escolhida para este projeto foi baseada nos **princípios de Kimball (Dimensional Modeling)**, utilizando um **Star Schema**.

### Justificativa da escolha
- O objetivo principal do projeto é **análise e visualização de dados**
- O contexto é **e-commerce**, com forte uso de métricas, séries temporais e indicadores de performance
- Os dados já passaram por etapas de **integração, qualidade e padronização**
- A abordagem Kimball favorece:
  - Simplicidade
  - Alto desempenho analítico
  - Facilidade de uso em ferramentas de BI (ex.: Metabase/Dadosfera)

Outras abordagens, como **Data Vault**, seriam mais indicadas para cenários de auditoria pesada ou múltiplas fontes altamente voláteis, o que não é o foco principal deste case.

---

## 6.2 Definição do Grão

O **grão do modelo** foi definido como:

> **Uma entrega (viagem de táxi reinterpretada como entrega logística)**

Cada registro da tabela fato representa uma entrega individual, realizada em um ponto específico do tempo, associada a localizações, fornecedor e método de pagamento.

---

## 6.3 Estrutura do Modelo Dimensional

### 6.3.1 Tabela Fato

**FACT_TRIPS (Fato_Entregas)**  
Contém as métricas quantitativas do processo de entrega.

**Principais métricas:**
- `trip_distance`
- `fare_amount`
- `tip_amount`
- `tolls_amount`
- `total_amount`
- `congestion_surcharge`
- `trip_duration_seconds`

**Chaves estrangeiras:**
- `time_id`
- `pickup_location_id`
- `dropoff_location_id`
- `vendor_id`
- `payment_type_id`

---

### 6.3.2 Tabelas Dimensão

#### DIM_TIME
Responsável pela análise temporal.

Campos:
- `time_id`
- `date`
- `day`
- `month`
- `year`
- `hour`
- `weekday`

---

#### DIM_LOCATION
Representa zonas e regiões geográficas.

Campos:
- `location_id`
- `zone`
- `borough`

---

#### DIM_VENDOR
Identifica o fornecedor/operador da entrega.

Campos:
- `vendor_id`
- `vendor_description`

---

#### DIM_PAYMENT
Descreve o método de pagamento utilizado.

Campos:
- `payment_type_id`
- `payment_description`

---
As dimensões de Tempo e Localização foram derivadas a partir dos dados transacionais existentes, sem perda de informação, garantindo escalabilidade, governança e reutilização dos dados.

---

## 6.4 Visões Finais dos Dados

### Visão 1 – Visão Operacional (Performance)
Foco em eficiência e acompanhamento do negócio no dia a dia.

Exemplos de análises:
- Volume de entregas por período
- Receita total e média
- Duração média das entregas
- Distância média percorrida
- Performance por região

Usuários-alvo: **Operações e Logística**

---

### Visão 2 – Visão Analítica / Estratégica
Foco em padrões, tendências e apoio à tomada de decisão.

Exemplos de análises:
- Séries temporais de receita
- Comparação entre regiões
- Distribuição por métodos de pagamento
- Identificação de horários de pico
- Tendências de crescimento ou queda

Usuários-alvo: **Gestão e Estratégia**

---

## 6.5 Bônus – Diagrama do Data Warehouse

O diagrama abaixo representa a camada final do Data Warehouse proposto, seguindo um esquema estrela.

```mermaid
erDiagram
    FACT_TRIPS {
        int trip_id
        int vendor_id
        int pickup_location_id
        int dropoff_location_id
        int payment_type_id
        int time_id
        float trip_distance
        float fare_amount
        float tip_amount
        float total_amount
        float trip_duration_seconds
    }

    DIM_TIME {
        int time_id
        date date
        int day
        int month
        int year
        int hour
        string weekday
    }

    DIM_LOCATION {
        int location_id
        string zone
        string borough
    }

    DIM_VENDOR {
        int vendor_id
        string vendor_description
    }

    DIM_PAYMENT {
        int payment_type_id
        string payment_description
    }

    FACT_TRIPS }o--|| DIM_TIME : time_id
    FACT_TRIPS }o--|| DIM_LOCATION : pickup_location
    FACT_TRIPS }o--|| DIM_LOCATION : dropoff_location
    FACT_TRIPS }o--|| DIM_VENDOR : vendor
    FACT_TRIPS }o--|| DIM_PAYMENT : payment
