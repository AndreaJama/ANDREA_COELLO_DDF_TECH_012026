
# Item 5 – Feature Engineering com GenAI (LLM)

## Visão Geral

Este item do case tem como objetivo demonstrar a capacidade de transformar **dados textuais desestruturados** em **features estruturadas**, utilizando **Modelos de Linguagem de Grande Porte (LLMs)**, preparando a base para análises posteriores e visualização de dados.

O foco foi a construção de um **pipeline robusto, reproduzível e defensivo**, priorizando qualidade e clareza do processo em vez de volume massivo de dados.

---

## Dataset de Entrada

- **Arquivo**: `corpus-simple.jsonl`
- **Formato**: JSON Lines
- **Campos originais**:
  - `docid`
  - `title`
  - `text` (descrição do produto)

As descrições são longas e não estruturadas, inviabilizando análises diretas sem processamento semântico.

---

## Estratégia Utilizada

- Uso de **LLM local (Mistral 7B Instruct – quantizado)** executado no **Google Colab**
- Leitura do dataset em **streaming**
- Processamento **registro a registro**
- Salvamento **incremental em batches**
- Limitação intencional do volume para validação do pipeline

> O objetivo foi validar o método de feature engineering com GenAI e garantir que o pipeline esteja pronto para escalar, mesmo sem processar todo o dataset original.

---

## Prompt de Extração de Features

```text
You are a data extraction system.

Given a product TITLE and DESCRIPTION, extract structured features.
Return ONLY valid JSON.
Do not add explanations.

JSON format:
{
  "category": "",
  "material": "",
  "compatibility": "",
  "features": {
    "key_features": [],
    "functions": [],
    "certifications": [],
    "other_attributes": []
  }
}
```

## 5. Features Geradas

A partir da inferência do LLM, as seguintes features estruturadas foram extraídas das descrições textuais dos produtos:

| Coluna | Descrição |
|------|---------|
| product_id | Identificador do produto |
| title | Título original do produto |
| category | Categoria inferida pelo LLM |
| material | Material principal identificado |
| compatibility | Compatibilidade do produto |
| key_features | Principais características |
| functions | Funções do produto |
| other_attributes | Atributos adicionais relevantes |
| processing_timestamp | Timestamp do processamento |

Essas colunas permitem análises categóricas, comparativas e temporais dos produtos.

---

## 6. Base Final Gerada

- **Arquivo**: `products_features_item5.csv`
- **Formato**: CSV
- **Quantidade de registros**: 43
- **Status**: Base estruturada e pronta para análise

Esta base representa o **output final do Item 5**, sendo utilizada como insumo para a etapa de análise e visualização de dados.

---

## 7. Arquivos de Programação Utilizados

Os seguintes arquivos foram utilizados na implementação deste item:

- **`feature_engineering_llm.ipynb`**  
  Notebook executado no Google Colab contendo:
  - leitura do dataset em streaming
  - definição e validação do prompt
  - execução do LLM local
  - limpeza defensiva da saída em JSON
  - flatten das features
  - salvamento incremental da base final

- **`products_features_item5.csv`**  
  Base final estruturada gerada pelo pipeline.

---

## 8. Fluxo do Pipeline

```mermaid
flowchart TD
    A[Dataset JSONL<br/>corpus-simple.jsonl] --> B[Leitura em streaming]
    B --> C[Construção do prompt]
    C --> D[LLM local<br/>Mistral 7B Instruct]
    D --> E[Resposta em texto]
    E --> F[Limpeza defensiva do JSON]
    F --> G[Extração de features]
    G --> H[Flatten dos atributos]
    H --> I[Salvamento incremental<br/>CSV]
    I --> J[Base estruturada<br/>products_features_item5.csv]

