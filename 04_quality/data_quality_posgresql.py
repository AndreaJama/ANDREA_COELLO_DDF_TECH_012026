"""
Item 4 - Data Quality (PostgreSQL)
Validação completa com Great Expectations (API Validator)
Escopo equivalente à análise local (22 regras)
"""

# ============================================================
# 1. IMPORTS
# ============================================================

import pandas as pd
import great_expectations as gx
from sqlalchemy import create_engine

# ============================================================
# 2. CONEXÃO COM POSTGRESQL (SUPABASE)
# ============================================================

DB_USER = "postgres.ychjbgtcwocpioaicuwb"
DB_PASSWORD = "SUA_SENHA_AQUI"
DB_HOST = "aws-1-us-east-2.pooler.supabase.com"
DB_PORT = 6543
DB_NAME = "postgres"

engine = create_engine(
    "postgresql://postgres.ychjbgtcwocpioaicuwb:1andrisAJ26*@aws-1-us-east-2.pooler.supabase.com:6543/postgres"
)

query = """
SELECT
    vendorid AS "VendorID",
    tpep_pickup_datetime,
    tpep_dropoff_datetime,
    passenger_count,
    trip_distance,
    ratecodeid AS "RatecodeID",
    store_and_fwd_flag,
    pulocationid AS "PULocationID",
    dolocationid AS "DOLocationID",
    payment_type,
    fare_amount,
    extra,
    mta_tax,
    tip_amount,
    tolls_amount,
    improvement_surcharge,
    total_amount,
    congestion_surcharge,
    airport_fee AS "Airport_fee"
FROM public.nyc_taxi_trips_2024_01;
"""

df = pd.read_sql(query, engine)

print("Dados carregados do PostgreSQL.")
print(f"Total de registros: {len(df)}")

# ============================================================
# 3. PREPARAÇÃO DOS DADOS
# ============================================================

df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])

df["trip_duration_seconds"] = (
    df["tpep_dropoff_datetime"] - df["tpep_pickup_datetime"]
).dt.total_seconds()

# ============================================================
# 4. GREAT EXPECTATIONS - VALIDATOR
# ============================================================

context = gx.get_context()
validator = context.sources.pandas_default.read_dataframe(df)

# ============================================================
# 5. REGRAS DE QUALIDADE (22 EXPECTATIONS)
# ============================================================

print("\nAplicando regras de qualidade (escopo completo)...")

# ------------------------
# COMPLETUDE (7)
# ------------------------
validator.expect_column_values_to_not_be_null("VendorID")
validator.expect_column_values_to_not_be_null("tpep_pickup_datetime")
validator.expect_column_values_to_not_be_null("tpep_dropoff_datetime")
validator.expect_column_values_to_not_be_null("passenger_count")
validator.expect_column_values_to_not_be_null("trip_distance")
validator.expect_column_values_to_not_be_null("fare_amount")
validator.expect_column_values_to_not_be_null("total_amount")

# ------------------------
# VALIDADE / FAIXA (11)
# ------------------------
validator.expect_column_values_to_be_between("VendorID", min_value=1)
validator.expect_column_values_to_be_between("passenger_count", min_value=1, max_value=8)
validator.expect_column_values_to_be_between("trip_distance", min_value=0)
validator.expect_column_values_to_be_between("fare_amount", min_value=0)
validator.expect_column_values_to_be_between("extra", min_value=0)
validator.expect_column_values_to_be_between("mta_tax", min_value=0)
validator.expect_column_values_to_be_between("tip_amount", min_value=0)
validator.expect_column_values_to_be_between("tolls_amount", min_value=0)
validator.expect_column_values_to_be_between("improvement_surcharge", min_value=0)
validator.expect_column_values_to_be_between("congestion_surcharge", min_value=0)
validator.expect_column_values_to_be_between("Airport_fee", min_value=0)

# ------------------------
# DOMÍNIO (2)
# ------------------------
validator.expect_column_values_to_be_in_set(
    "payment_type", [1, 2, 3, 4, 5, 6]
)

validator.expect_column_values_to_be_in_set(
    "store_and_fwd_flag", ["Y", "N"]
)

# ------------------------
# CONSISTÊNCIA (2)
# ------------------------
validator.expect_column_values_to_be_between(
    "trip_duration_seconds",
    min_value=0
)

validator.expect_column_values_to_be_between(
    "total_amount",
    min_value=0
)

# ============================================================
# 6. EXECUÇÃO DA VALIDAÇÃO
# ============================================================

print("\nExecutando validação...")
results = validator.validate()

# ============================================================
# 7. RESUMO DOS RESULTADOS
# ============================================================

print("\n=== RELATÓRIO DE QUALIDADE DE DADOS - POSTGRESQL ===")

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

# ============================================================
# 8. GERAÇÃO DO RELATÓRIO
# ============================================================

with open("data_quality_report_postgres_full.txt", "w", encoding="utf-8") as f:
    f.write("RELATÓRIO DE QUALIDADE DE DADOS - POSTGRESQL\n\n")
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

print("\nRelatório gerado: data_quality_report_postgres_full.txt")
