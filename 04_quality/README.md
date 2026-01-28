# Great Expectations

O **Great Expectations** é um pacote de **validação de dados** em Python.  
Ele ajuda equipes a garantir que os dados usados em análises, pipelines ou modelos de machine learning estejam corretos, consistentes e confiáveis.

## ✨ Principais funções
- **Validação de dados**: definir regras (*expectations*) sobre como os dados devem se comportar.  
  Exemplo: uma coluna não pode ter valores nulos ou deve estar dentro de um intervalo específico.  
- **Documentação automática**: gera relatórios claros e interativos sobre a qualidade dos dados.  
- **Integração com pipelines**: funciona com ferramentas como Airflow, dbt, Spark e Pandas.  
- **Monitoramento contínuo**: detecta problemas de qualidade antes que impactem relatórios ou modelos.  

👉 Em resumo: o Great Expectations é como **testes unitários para dados**, garantindo que eles estejam sempre no formato e qualidade esperados.

---

## 📋 Requisitos
- **Python** 3.8 ou superior  
- **pip** atualizado  python.exe -m pip install --upgrade pip
- Ambiente virtual recomendado (venv ou conda)  

---

## ⚙️ Instalação

### Usando pip
```bash
pip install great-expectations

pip install great_expectations 
pip install --upgrade great-expectations
pip install "sqlalchemy<2.0"  
great_expectations init

•	É um comando de inicialização do Great Expectations.
•	Ele cria uma estrutura de pastas e arquivos chamada great_expectations/ no seu projeto.
•	Essa estrutura serve para você configurar, salvar expectativas, conectar fontes de dados e rodar validações.
