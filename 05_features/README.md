
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
