import pandas as pd

url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"

df = pd.read_parquet(url)

print(df.shape)
print(df.head())
