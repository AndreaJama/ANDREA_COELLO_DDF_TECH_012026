# Item 2.1 – Integração de Dados na Dadosfera

Nesta etapa, foi realizado o carregamento da base de dados proposta para a plataforma Dadosfera, utilizando o módulo de Coleta.

## Fonte de Dados
Base pública da NYC Taxi & Limousine Commission (TLC), contendo milhões de registros de viagens, reinterpretadas neste projeto como entregas logísticas no contexto de e-commerce.


### Preparação do Arquivo

Os dados utilizados são provenientes da base pública da NYC Taxi & Limousine Commission, disponibilizados no formato Parquet. Para fins de ingestão na Dadosfera, foi selecionado um arquivo mensal (janeiro/2023 – táxi amarelo), garantindo volume superior a 100.000 registros.

Antes da importação, foi realizada uma validação básica de esquema e volume, seguida da conversão do arquivo para o formato CSV (UTF-8), visando facilitar o carregamento manual na plataforma.

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

<p align="center">
  <img src="prints/dataset_catalogo.png" width="600"/>
</p>

## Microtransformação 

Após a ingestão, foi aplicada uma microtransformação para padronização dos campos e criação de atributos derivados, como o tempo de entrega em minutos, facilitando análises posteriores.


