"""
Item 4 - Data Quality
Execução de validações utilizando Great Expectations
com dados provenientes de PostgreSQL
"""

# =========================
# 1. Imports
# =========================

import pandas as pd
import great_expectations as gx
from sqlalchemy import create_engine

# =========================
# 2. Conexão com PostgreSQL
# =========================

# ⚠️ Ajuste os dados de conexão

engine = create_engine(
    "postgresql://postgres.ychjbgtcwocpioaicuwb:1andrisAJ26*@aws-1-us-east-2.pooler.supabase.com:6543/postgres"
)

query = """
SELECT *
FROM nyc_taxi_trips_2024_01
"""

df = pd.read_sql(query, engine)

print("Dados carregados do PostgreSQL com sucesso.")
print(f"Total de registros: {len(df)}")

# =========================
# 3. Preparação dos dados
# =========================

df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

df["trip_duration_seconds"] = (
    df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
).dt.total_seconds()

# =========================
# 4. Inicialização do Great Expectations
# =========================

context = gx.get_context()

validator = context.sources.pandas_default.read_dataframe(df)

# =========================
# 5. Regras de Qualidade
# =========================

print("\nAplicando regras de qualidade...")

# --- COMPLETUDE ---
validator.expect_column_values_to_not_be_null("VendorID")
validator.expect_column_values_to_not_be_null("tpep_pickup_datetime")
validator.expect_column_values_to_not_be_null("tpep_dropoff_datetime")
validator.expect_column_values_to_not_be_null("passenger_count")
validator.expect_column_values_to_not_be_null("trip_distance")
validator.expect_column_values_to_not_be_null("fare_amount")
validator.expect_column_values_to_not_be_null("total_amount")

# --- VALIDADE ---
validator.expect_column_values_to_be_between("VendorID", min_value=1)
validator.expect_column_values_to_be_between("passenger_count", min_value=1, max_value=8)
validator.expect_column_values_to_be_between("trip_distance", min_value=0)
validator.expect_column_values_to_be_between("fare_amount", min_value=0)
validator.expect_column_values_to_be_between("total_amount", min_value=0)

# --- DOMÍNIO ---
validator.expect_column_values_to_be_in_set("payment_type", [1, 2, 3, 4, 5, 6])
validator.expect_column_values_to_be_in_set("store_and_fwd_flag", ["Y", "N"])

# --- CONSISTÊNCIA ---
validator.expect_column_values_to_be_between(
    "trip_duration_seconds",
    min_value=0
)

# =========================
# 6. Execução da Validação
# =========================

print("\nExecutando validação...")

results = validator.validate()

# =========================
# 7. Resumo dos Resultados
# =========================

print("\n=== RESUMO DO RELATÓRIO DE QUALIDADE ===")

status = "SUCESSO" if results.success else "FALHAS ENCONTRADAS"
print(f"Status geral: {status}")

total_rules = len(results.results)
failed_rules = [r for r in results.results if not r["success"]]

print(f"Total de regras avaliadas: {total_rules}")
print(f"Regras com falha: {len(failed_rules)}")

if failed_rules:
    print("\nDetalhamento das falhas:")
    for fail in failed_rules:
        expectation = fail["expectation_config"]["expectation_type"]
        column = fail["expectation_config"]["kwargs"].get("column", "N/A")
        unexpected = fail["result"].get("unexpected_count", "N/A")

        print(
            f"- Expectation: {expectation} | "
            f"Coluna: {column} | "
            f"Registros inesperados: {unexpected}"
        )

# =========================
# 8. Geração do Relatório
# =========================

with open("data_quality_report_postgres.txt", "w", encoding="utf-8") as f:
    f.write("RELATÓRIO DE QUALIDADE DE DADOS - PostgreSQL\n\n")
    f.write(f"Status geral: {status}\n")
    f.write(f"Total de regras avaliadas: {total_rules}\n")
    f.write(f"Regras com falha: {len(failed_rules)}\n\n")

    if failed_rules:
        f.write("Detalhamento das falhas:\n")
        for fail in failed_rules:
            expectation = fail["expectation_config"]["expectation_type"]
            column = fail["expectation_config"]["kwargs"].get("column", "N/A")
            unexpected = fail["result"].get("unexpected_count", "N/A")

            f.write(
                f"- Expectation: {expectation} | "
                f"Coluna: {column} | "
                f"Registros inesperados: {unexpected}\n"
            )

print("\nRelatório gerado: data_quality_report_postgresql.txt")

