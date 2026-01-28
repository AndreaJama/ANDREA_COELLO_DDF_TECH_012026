# Item 4 – Data Quality

## 4.1 Contexto

Após a integração e exploração dos dados transacionais utilizados no case (registros de viagens da NYC Taxi & Limousine Commission, utilizados como proxy de dados de e-commerce/logística), foi identificada a necessidade de avaliar e garantir a **qualidade dos dados** antes de seu uso em análises avançadas e modelos de IA.

Dados inconsistentes, incompletos ou semanticamente incorretos podem impactar negativamente:
- A performance de modelos de Machine Learning
- A confiabilidade de análises descritivas e prescritivas
- A tomada de decisão baseada em dados

Dessa forma, este item tem como objetivo definir e validar **regras explícitas de qualidade de dados**, seguindo boas práticas de governança e observabilidade recomendadas pela Dadosfera.

---

## 4.2 Abordagem adotada

A abordagem de Data Quality foi estruturada em duas etapas principais:

1. **Definição conceitual das regras de qualidade**, a partir do entendimento do domínio dos dados  
2. **Preparação técnica para validação automática**, utilizando a biblioteca *Great Expectations*

Neste estágio inicial, o foco está na **formalização das expectativas de qualidade**, antes da automação completa das validações.

---

## 4.3 Tipos de regras de qualidade

As regras de qualidade foram organizadas em quatro categorias principais:

- **Completude**  
  Verifica se campos críticos possuem valores nulos ou ausentes.

- **Validade / Faixa de valores**  
  Garante que os valores estejam dentro de limites aceitáveis.

- **Domínio (Enumeração)**  
  Restringe colunas a conjuntos conhecidos e válidos de valores.

- **Consistência**  
  Avalia relações lógicas entre colunas (ex.: datas, totais).

---

## 4.4 Visão geral dos dados analisados

Exemplo de registro utilizado como referência conceitual:

```text
VendorID = 2
tpep_pickup_datetime = 2024-01-20 13:31:30
tpep_dropoff_datetime = 2024-01-20 14:03:25
passenger_count = 2.0
trip_distance = 17.14
RatecodeID = 2.0
store_and_fwd_flag = N
PULocationID = 132
DOLocationID = 233
payment_type = 1
fare_amount = 70.0
extra = 0.0
mta_tax = 0.5
tip_amount = 8.27
tolls_amount = 6.94
improvement_surcharge = 1.0
total_amount = 90.96
congestion_surcharge = 2.5
Airport_fee = 1.75
```
## 4.5 Regras de qualidade por coluna
### 📌 Identificação e Tempo

| Coluna | Exemplo | Significado | Regras esperadas |
|------|--------|------------|------------------|
| VendorID | 2 | Identificador do fornecedor | Não nulo, inteiro positivo |
| tpep_pickup_datetime | 2024-01-20 13:31:30 | Início da viagem | Não nulo, timestamp válido |
| tpep_dropoff_datetime | 2024-01-20 14:03:25 | Fim da viagem | Não nulo, ≥ pickup |

Regra de consistência associada:
- `tpep_dropoff_datetime ≥ tpep_pickup_datetime`

### 📌 Passageiros e Distância

| Coluna | Exemplo | Significado | Regras esperadas |
|------|--------|------------|------------------|
| passenger_count | 2.0 | Número de passageiros | ≥ 1, valor inteiro |
| trip_distance | 17.14 | Distância percorrida | ≥ 0 |

### 📌 Tarifação e Códigos

| Coluna | Exemplo | Significado | Regras esperadas |
|------|--------|------------|------------------|
| RatecodeID | 2.0 | Código de tarifa | Dentro do domínio válido |
| payment_type | 1 | Tipo de pagamento | ∈ {1,2,3,4,5,6} |
| store_and_fwd_flag | N | Armazenamento offline | ∈ {'Y','N'} |

### 📌 Localização

| Coluna | Exemplo | Significado | Regras esperadas |
|------|--------|------------|------------------|
| PULocationID | 132 | Zona de embarque | Inteiro positivo |
| DOLocationID | 233 | Zona de desembarque | Inteiro positivo |

### 📌 Valores Monetários

| Coluna | Exemplo | Significado | Regras esperadas |
|------|--------|------------|------------------|
| fare_amount | 70.0 | Tarifa base | ≥ 0 |
| extra | 0.0 | Taxas extras | ≥ 0 |
| mta_tax | 0.5 | Taxa MTA | ≥ 0 |
| tip_amount | 8.27 | Gorjeta | ≥ 0 |
| tolls_amount | 6.94 | Pedágios | ≥ 0 |
| improvement_surcharge | 1.0 | Taxa de melhoria | ≥ 0 |
| congestion_surcharge | 2.5 | Taxa de congestionamento | ≥ 0 |
| Airport_fee | 1.75 | Taxa de aeroporto | ≥ 0 |
| total_amount | 90.96 | Valor total da corrida | ≥ 0 e ≥ fare_amount |

Regra de consistência associada:
- `total_amount ≥ fare_amount`
  
Essas regras representam o contrato de qualidade dos dados e servem como base
para a implementação das validações automáticas com Great Expectations nas
próximas etapas do projeto.

## 4.6 Validação automática de qualidade dos dados

Para a validação das regras de qualidade definidas conceitualmente, foi utilizada
a biblioteca **Great Expectations**, uma ferramenta open source amplamente adotada
para observabilidade e governança de dados.

O Great Expectations permite a definição declarativa de regras de qualidade
(*expectations*), que expressam de forma explícita o que se espera de cada coluna
do dataset, tais como:
- presença de valores (completude)
- faixas válidas
- domínios permitidos
- consistência entre colunas

Essas regras são executadas automaticamente sobre o dataset, gerando um relatório
de sucesso ou falha que pode ser utilizado para monitoramento contínuo da qualidade
dos dados.

As instruções de instalação do pacote e configuração do ambiente estão descritas
no arquivo:

```text
great-expectations.md
