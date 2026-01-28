"""
Data Quality Report - NYC Taxi Trips (Local)

Avaliação de qualidade de dados utilizando Great Expectations
a partir de um arquivo CSV local, simulando a camada Silver
de um Data Lake.
"""

# =========================
# 1. Imports
# =========================

import pandas as pd
import great_expectations as gx

# =========================
# 2. Leitura do CSV
# =========================

df = pd.read_csv("nyc_taxi_trips_2024_01.csv")

print("CSV carregado com sucesso.")
print(f"Total de registros: {len(df)}")
print("\nPrimeiras linhas:")
print(df.head())

# =========================
# 3. Inicialização do Great Expectations
# =========================

context = gx.get_context()

validator = context.sources.pandas_default.read_dataframe(df)

print("\nGreat Expectations inicializado com sucesso.")
print("Validator criado e pronto para receber regras de qualidade.")
