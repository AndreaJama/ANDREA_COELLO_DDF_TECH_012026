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

### Microtransformação (Bônus)

A Dadosfera adota o paradigma ELT, permitindo a aplicação de microtransformações no momento da ingestão de dados provenientes de fontes transacionais SQL.

No contexto deste projeto, a microtransformação de criptografia (hash) seria aplicada sobre a coluna `VendorID`, com o objetivo de anonimizar identificadores sensíveis mantendo a consistência analítica dos dados.

Devido ao uso de importação manual de arquivos CSV (coleta única), a aplicação prática da microtransformação não foi executada na interface, sendo o conceito, a escolha da coluna e o impacto documentados conforme as boas práticas da plataforma.


