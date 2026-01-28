

"""
Item 4 - Data Quality (PostgreSQL - CDM)
Validação da tabela canônica nyc_taxi_trips_2024_01_cdm
Great Expectations - API Validator
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

#engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

engine = create_engine(
    "postgresql://postgres.ychjbgtcwocpioaicuwb:1andrisAJ26*@aws-1-us-east-2.pooler.supabase.com:6543/postgres"
)

query = """
SELECT
    vendor_id,
    pickup_datetime,
    dropoff_datetime,
    trip_duration_seconds,
    passenger_count,
    trip_distance_miles,
    pickup_location_id,
    dropoff_location_id,
    rate_code,
    payment_type,
    fare_amount,
    extra_amount,
    tax_amount,
    tip_amount,
    tolls_amount,
    improvement_surcharge,
    congestion_surcharge,
    airport_fee,
    total_amount
FROM public.nyc_taxi_trips_2024_01_cdm;
"""

df = pd.read_sql(query, engine)

print("Dados CDM carregados do PostgreSQL.")
print(f"Total de registros: {len(df)}")

# ============================================================
# 3. GREAT EXPECTATIONS - VALIDATOR
# ============================================================

context = gx.get_context()
validator = context.sources.pandas_default.read_dataframe(df)

# ============================================================
# 4. REGRAS DE QUALIDADE (22 EXPECTATIONS - CDM)
# ============================================================

print("\nAplicando regras de qualidade (CDM)...")

# ------------------------
# COMPLETUDE (6)
# ------------------------
validator.expect_column_values_to_not_be_null("vendor_id")
validator.expect_column_values_to_not_be_null("pickup_datetime")
validator.expect_column_values_to_not_be_null("dropoff_datetime")
validator.expect_column_values_to_not_be_null("trip_duration_seconds")
validator.expect_column_values_to_not_be_null("passenger_count")
validator.expect_column_values_to_not_be_null("total_amount")

# ------------------------
# VALIDADE / FAIXA (12)
# ------------------------
validator.expect_column_values_to_be_between("passenger_count", 1, 8)
validator.expect_column_values_to_be_between("trip_distance_miles", 0)
validator.expect_column_values_to_be_between("fare_amount", 0)
validator.expect_column_values_to_be_between("extra_amount", 0)
validator.expect_column_values_to_be_between("tax_amount", 0)
validator.expect_column_values_to_be_between("tip_amount", 0)
validator.expect_column_values_to_be_between("tolls_amount", 0)
validator.expect_column_values_to_be_between("improvement_surcharge", 0)
validator.expect_column_values_to_be_between("congestion_surcharge", 0)
validator.expect_column_values_to_be_between("airport_fee", 0)
validator.expect_column_values_to_be_between("total_amount", 0)
validator.expect_column_values_to_be_between(
    "trip_duration_seconds", 0, 86400
)

# ------------------------
# DOMÍNIO (3)
# ------------------------
validator.expect_column_values_to_be_in_set(
    "payment_type", [1, 2, 3, 4, 5, 6]
)

validator.expect_column_values_to_be_between(
    "rate_code", 1, 6
)

validator.expect_column_values_to_be_in_set(
    "pickup_location_id",
    list(range(1, 266))
)

# ------------------------
# CONSISTÊNCIA (1)
# ------------------------
validator.expect_column_values_to_be_between(
    "dropoff_location_id",
    1, 265
)

# ============================================================
# 5. EXECUÇÃO DA VALIDAÇÃO
# ============================================================

print("\nExecutando validação...")
results = validator.validate()

# ============================================================
# 6. RESUMO DOS RESULTADOS
# ============================================================

print("\n=== RELATÓRIO DE QUALIDADE DE DADOS - POSTGRESQL (CDM) ===")

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
# 7. GERAÇÃO DO RELATÓRIO
# ============================================================

with open("data_quality_report_postgres_cdm.txt", "w", encoding="utf-8") as f:
    f.write("RELATÓRIO DE QUALIDADE DE DADOS - POSTGRESQL (CDM)\n\n")
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

print("\nRelatório gerado: data_quality_report_postgres_cdm.txt")
