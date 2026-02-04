# Item 2.1 – Integração de Dados na Dadosfera

Nesta etapa, foi realizado o carregamento da base de dados proposta para a plataforma Dadosfera, utilizando o módulo de Coleta.

## Fonte de Dados
Base pública da NYC Taxi & Limousine Commission (TLC), contendo milhões de registros de viagens, reinterpretadas neste projeto como entregas logísticas no contexto de e-commerce.

## Preparação do Arquivo para Ingestão

Antes da importação dos dados na Dadosfera, foi realizada uma validação básica da base de dados original em formato Parquet, incluindo verificação de volume e estrutura.

Para facilitar a ingestão manual na plataforma, foi gerado um arquivo CSV a partir de uma amostra de 200.000 registros, mantendo o dado bruto sem transformações analíticas.

O script utilizado para essa preparação encontra-se em:
- `scripts/prepare_nyc_taxi_data.py`

## Método de Coleta
Foi utilizada a importação manual de arquivos CSV, uma vez que se trata de um dataset estático para fins de análise e desenvolvimento do case.

### Importação Manual de Arquivos

Nesta etapa, os dados foram carregados na plataforma Dadosfera por meio da funcionalidade **Importar arquivos**, recomendada para bases de dados estáticas ou que não necessitam de atualização recorrente.

<img src="importar.png" alt="importar" width="400"/>

<img src="novo_arquivo.png" alt="novo_arquivo" width="600"/>

A origem dos dados é o dispositivo local, caracterizando uma coleta única, sem agendamento automático.

### Configurações da Importação

O arquivo importado segue as especificações suportadas pela plataforma, conforme detalhado abaixo:

| Configuração            | Valor Utilizado |
|-------------------------|-----------------|
| Tipo de arquivo         | CSV |
| Codificação             | UTF-8 |
| Separador               | `,` |
| Cabeçalho               | Sim |
| Tamanho do arquivo      | Inferior a 250 MB |

<img src="configuracoes.png" alt="configuracoes" width="800"/>

Durante o processo de importação, foi definido um nome e uma descrição para o dataset, permitindo melhor contextualização e governança dos dados no catálogo da plataforma.

<img src="informacoes.png" alt="informacoes" width="800"/>

<img src="arquivo_carregado.png" alt="arquivo_carregado" width="800"/>

## Acompanhar importação
Verifique o Status da extração do arquivo do seu dispositivo:

<img src="status1.png" alt="status1" width="400"/>

<img src="final_status.png" alt="final_status" width="600"/>

Após a conclusão da importação, o dataset ficou disponível para visualização e consulta no **Catálogo de Dados** da Dadosfera.

[Catálogo](https://app.dadosfera.ai/pt-BR/catalog/data-assets/34bfb383-60a8-4e70-af64-dc9d53f595f7)

## ⭐ Bônus – Microtransformação com PostgreSQL (Supabase)
 
A Dadosfera adota o paradigma ELT, permitindo a aplicação de microtransformações no momento da ingestão de dados provenientes de fontes transacionais SQL.

No contexto deste projeto, a microtransformação de criptografia (hash) seria aplicada sobre a coluna `VendorID`, com o objetivo de anonimizar identificadores sensíveis mantendo a consistência analítica dos dados.

Devido ao uso de importação manual de arquivos CSV (coleta única), a aplicação prática da microtransformação não foi executada na interface, sendo o conceito, a escolha da coluna e o impacto documentados conforme as boas práticas da plataforma.

---

### 🔹 Arquitetura adotada

A solução segue o paradigma **ELT (Extract, Load, Transform)**:

- **Extract**: leitura de dados a partir de uma base PostgreSQL transacional  
- **Load**: ingestão dos dados no Data Lake da Dadosfera  
- **Transform**: aplicação de microtransformações durante o processo de coleta  

Essa abordagem permite maior flexibilidade analítica, além de reforçar práticas de **governança, segurança e rastreabilidade dos dados**.

---

### 🔹 Configuração da fonte PostgreSQL

A fonte de dados foi cadastrada na Dadosfera com os seguintes parâmetros:

- **Banco de dados**: PostgreSQL (Supabase – Cloud)
- **Tipo de conexão**: Direta
- **Endpoint**: via Transaction Pooler (IPv4 compatível)
- **Porta**: 6543
- **Database**: `postgres`
- **Usuário**: usuário padrão do Supabase
- **Schema coletado**: `public`\
  
![conf_postgreSQL](conf_postgreSQL.png)

---

### 🔹 Configuração da pipeline

Na criação da pipeline:

- Foi selecionado o objeto **`nyc_taxi_trips_2024_01`**
- Modo de sincronização configurado como **Full Load**

![info_pipeline_postgresql](info_pipeline_postgresql.png)

**Justificativa**:
- Dataset histórico
- Base estática para análise exploratória e analítica
- Simplificação do controle de carga para o escopo do case

![pipeline_schema](pipeline_schema.png)

![sel_objeto](sel_objeto.png)

![fullload](fullload.png)

---

### 🔹 Microtransformação aplicada (Hash)

Durante a configuração da pipeline, foi aplicada uma **microtransformação do tipo _Criptografar (Hash)_** sobre a coluna:

- **Coluna**: `VendorID`
- **Objetivo**:
  - Anonimizar identificadores sensíveis
  - Preservar consistência entre valores repetidos
  - Permitir análises agregadas sem exposição de dados sensíveis

A microtransformação é aplicada **evento a evento** durante a ingestão, garantindo que valores iguais resultem no mesmo hash.

![microtransformacao](microtransformacao.png)

---

### 🔹 Agendamento e execução

A pipeline foi configurada como **Única extração**, executando a coleta imediatamente após a criação.

Essa escolha foi feita por se tratar de um **dataset estático**, adequado ao contexto de demonstração técnica do case, mantendo a possibilidade de reexecução manual se necessário.

![unica_extracao](unica_extracao.png)

---

### 🔹 Resultado final

Após a execução da pipeline:

- Os dados foram ingeridos com sucesso na Dadosfera
- O dataset foi automaticamente **catalogado como Data Asset**
- A coluna `VendorID` passou a apresentar valores **anonimizados (hash)**
- As demais colunas permaneceram intactas, garantindo qualidade e integridade dos dados

![pipeline_criada](pipeline_criada.png)

![pipeline_at](pipeline_at.png)

[Pipeline](https://app.dadosfera.ai/pt-BR/collect/pipelines/c053bd76-e050-4527-8bb7-15f6d735344f)
---

### 🔹 Considerações finais

Este bônus demonstra, de forma prática:

- Integração entre banco transacional cloud e Data Lake
- Aplicação de **boas práticas de ELT**
- Uso de microtransformações para **segurança e privacidade**
- Capacidade da plataforma em realizar ingestão, transformação e catalogação de forma integrada

O processo reforça uma visão orientada a **governança de dados**, **qualidade** e **escalabilidade**, alinhada a cenários reais de produção.



