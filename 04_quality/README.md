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



great_expectations init
