
import pandas as pd

# Leitura do arquivo Parquet original
df = pd.read_parquet("yellow_tripdata_2023-01.parquet")

# Validação básica de volume e estrutura
print(df.shape)
print(df.head())

# Amostragem para facilitar ingestão manual na plataforma
df_sample = df.sample(200000, random_state=42)

# Exportação para CSV
df_sample.to_csv(
    "nyc_taxi_trips_2023_01.csv",
    index=False,
    encoding="utf-8"
)
