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

csv_path = "data/nyc_taxi_trips_2024_01.csv"
