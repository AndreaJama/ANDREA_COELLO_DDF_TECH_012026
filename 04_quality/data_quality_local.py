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

# =========================
# PASSO 4 - Regras de Qualidade dos Dados
# =========================

print("\nAplicando regras de qualidade dos dados...")

# -------------------------------------------------
# 4.1 COMPLETUDE
# Campos críticos não podem ser nulos
# -------------------------------------------------

print("→ Regras de completude")

validator.expect_column_values_to_not_be_null("VendorID")
validator.expect_column_values_to_not_be_null("tpep_pickup_datetime")
validator.expect_column_values_to_not_be_null("tpep_dropoff_datetime")
validator.expect_column_values_to_not_be_null("passenger_count")
validator.expect_column_values_to_not_be_null("trip_distance")
validator.expect_column_values_to_not_be_null("fare_amount")
validator.expect_column_values_to_not_be_null("total_amount")

# -------------------------------------------------
# 4.2 VALIDADE / FAIXA DE VALORES
# Valores numéricos devem estar dentro de limites aceitáveis
# -------------------------------------------------

print("→ Regras de validade (faixa de valores)")

validator.expect_column_values_to_be_between(
    "VendorID", min_value=1
)

validator.expect_column_values_to_be_between(
    "passenger_count", min_value=1, max_value=8
)

validator.expect_column_values_to_be_between(
    "trip_distance", min_value=0
)

validator.expect_column_values_to_be_between(
    "fare_amount", min_value=0
)

validator.expect_column_values_to_be_between(
    "extra", min_value=0
)

validator.expect_column_values_to_be_between(
    "mta_tax", min_value=0
)

validator.expect_column_values_to_be_between(
    "tip_amount", min_value=0
)

validator.expect_column_values_to_be_between(
    "tolls_amount", min_value=0
)

validator.expect_column_values_to_be_between(
    "improvement_surcharge", min_value=0
)

validator.expect_column_values_to_be_between(
    "congestion_surcharge", min_value=0
)

validator.expect_column_values_to_be_between(
    "Airport_fee", min_value=0
)

validator.expect_column_values_to_be_between(
    "total_amount", min_value=0
)

# -------------------------------------------------
# 4.3 DOMÍNIO (ENUMERAÇÕES)
# Conjuntos fechados de valores válidos
# -------------------------------------------------

print("→ Regras de domínio")

validator.expect_column_values_to_be_in_set(
    "payment_type", [1, 2, 3, 4, 5, 6]
)

validator.expect_column_values_to_be_in_set(
    "store_and_fwd_flag", ["Y", "N"]
)

# -------------------------------------------------
# 4.4 CONSISTÊNCIA TEMPORAL
# Relações lógicas entre colunas
# -------------------------------------------------

df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

df["trip_duration_seconds"] = (
    df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
).dt.total_seconds()

print("→ Regras de consistência")

# Duração da corrida não pode ser negativa
validator.expect_column_values_to_be_between(
    "trip_duration_seconds", min_value=0
)

# Valor total deve ser >= tarifa base
validator.expect_column_values_to_be_between(
    "total_amount",
    min_value=df["fare_amount"].min()
)

print("Regras de qualidade aplicadas com sucesso.")

# =========================
# PASSO 5 - Execução da Validação
# =========================

print("\nExecutando validação das regras de qualidade...")

results = validator.validate()

print("Validação executada.")

# =========================
# PASSO 6 - Resumo dos Resultados
# =========================

print("\n=== RESUMO DO RELATÓRIO DE QUALIDADE ===")

# Status geral
if results.success:
    print("Status geral: SUCESSO ✅")
else:
    print("Status geral: FALHAS ENCONTRADAS ⚠️")

total_expectations = len(results.results)
failed_expectations = [r for r in results.results if not r["success"]]

print(f"Total de regras avaliadas: {total_expectations}")
print(f"Regras com falha: {len(failed_expectations)}")

# Detalhamento das falhas
if failed_expectations:
    print("\nDetalhamento das regras com falha:")
    for fail in failed_expectations:
        expectation = fail["expectation_config"]["expectation_type"]
        column = fail["expectation_config"]["kwargs"].get("column", "N/A")
        unexpected = fail["result"].get("unexpected_count", "N/A")

        print(
            f"- Expectation: {expectation} | "
            f"Coluna: {column} | "
            f"Registros inesperados: {unexpected}"
        )
else:
    print("\nNenhuma falha encontrada.")

# =========================
# Geração de Relatório de Qualidade
# =========================

report_path = "data_quality_report.txt"

with open(report_path, "w", encoding="utf-8") as f:
    f.write("RELATÓRIO DE QUALIDADE DE DADOS\n")
    f.write("NYC Taxi Trips - Janeiro/2024\n\n")

    f.write(f"Status geral: {'SUCESSO' if results.success else 'FALHAS ENCONTRADAS'}\n")
    f.write(f"Total de regras avaliadas: {total_expectations}\n")
    f.write(f"Regras com falha: {len(failed_expectations)}\n\n")

    if failed_expectations:
        f.write("Detalhamento das falhas:\n")
        for fail in failed_expectations:
            expectation = fail["expectation_config"]["expectation_type"]
            column = fail["expectation_config"]["kwargs"].get("column", "N/A")
            unexpected = fail["result"].get("unexpected_count", "N/A")

            f.write(
                f"- Expectation: {expectation} | "
                f"Coluna: {column} | "
                f"Registros inesperados: {unexpected}\n"
            )
    else:
        f.write("Nenhuma falha encontrada.\n")

print(f"\nRelatório gerado com sucesso: {report_path}")

