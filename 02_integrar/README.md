# Item 2.1 – Integração de Dados na Dadosfera

Nesta etapa, foi realizado o carregamento da base de dados proposta para a plataforma Dadosfera, utilizando o módulo de Coleta.

## Fonte de Dados
Base pública da NYC Taxi & Limousine Commission (TLC), contendo milhões de registros de viagens, reinterpretadas neste projeto como entregas logísticas no contexto de e-commerce.
![catalogo](dataset_catalogo.png)

## Preparação do Arquivo para Ingestão

Antes da importação dos dados na Dadosfera, foi realizada uma validação básica da base de dados original em formato Parquet, incluindo verificação de volume e estrutura.

Para facilitar a ingestão manual na plataforma, foi gerado um arquivo CSV a partir de uma amostra de 200.000 registros, mantendo o dado bruto sem transformações analíticas.

O script utilizado para essa preparação encontra-se em:
- `scripts/prepare_nyc_taxi_data.py`


## Método de Coleta
Foi utilizada a importação manual de arquivos CSV, uma vez que se trata de um dataset estático para fins de análise e desenvolvimento do case.

## Volume de Dados
O dataset carregado possui volume superior a 100.000 registros, atendendo plenamente aos requisitos do case.

## Evidências da Importação
<p align="center">
  <img src="prints/upload_arquivo.png" width="600"/>
</p>

<p align="center">
  <img src="prints/status_importacao.png" width="600"/>
</p>



## Microtransformação 

Após a ingestão, foi aplicada uma microtransformação para padronização dos campos e criação de atributos derivados, como o tempo de entrega em minutos, facilitando análises posteriores.


