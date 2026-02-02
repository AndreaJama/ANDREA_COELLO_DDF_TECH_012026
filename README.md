# Case Técnico – Plataforma de Dados para E-commerce
**Candidato:** Andrea Coello  
**Vaga:** Analista de Dados  
**Empresa:** Dadosfera  

## Objetivo
Este projeto apresenta a implementação de uma Plataforma de Dados utilizando a Dadosfera, com foco em centralizar fontes de dados de um e-commerce para análises descritivas, prescritivas e uso de IA.

## Contexto do Negócio
O cliente é uma empresa de e-commerce com alto investimento em mídia paga, operação logística própria e necessidade de decisões baseadas em dados confiáveis e acessíveis.

## Estrutura do Projeto
O repositório está organizado seguindo o ciclo de vida dos dados proposto pela Dadosfera:
1. Integrar  
2. Processar  
3. Explorar  
4. Qualidade dos dados 
5. Features  
6. Modelagem 
7. Dashboard 

## Tecnologias Utilizadas
- SQL
- Python
- Google Colab
- Github
- Supabase - PostgreSQL
- Mermaid

## Fluxograma do projeto

```mermaid
flowchart TB
    A["Iniciação do Projeto<br/>Kickoff com Stakeholders"] 
    --> B["Entendimento do Problema de Negócio<br/>Objetivos e KPIs"]

    B --> C["Levantamento de Dados<br/>Fontes, Volume e Estrutura"]

    C --> D["Planejamento Analítico<br/>Escopo, Riscos e Prioridades"]

    D --> E["Arquitetura de Dados<br/>Plataforma Dadosfera"]

    E --> F["Ingestão e Integração de Dados<br/>Carga em Banco Analítico"]

    F --> G["Qualidade e Tratamento de Dados<br/>Validações e Padronizações"]

    G --> H["Modelagem Analítica<br/>Visões para Análise"]

    H --> I["Exploração e Consulta de Dados<br/>SQL e Métricas"]

    I --> J["Análise de Dados e Visualização<br/>Dashboards e Insights"]

    J --> K["Validação com Stakeholders<br/>Feedback e Ajustes"]

    K --> L["Entrega Final<br/>Dashboard, Documentação e Resultados"]

    %% Camadas avançadas (opcionais)
    J -.-> M["IA / LLMs<br/>Extração de Features Textuais"]
    M -.-> J

    J -.-> N["Data Apps<br/>Exploração Avançada"]
    
    %% Riscos e controles
    D -. Risco de Escopo .-> B
    G -. Qualidade de Dados .-> F
    J -. Adoção do Usuário .-> K
```
