--Tabela Staging

CREATE TABLE public.nyc_taxi_trips_2024_01_stg (
    vendorid TEXT,
    tpep_pickup_datetime TEXT,
    tpep_dropoff_datetime TEXT,
    passenger_count TEXT,
    trip_distance NUMERIC,
    ratecodeid TEXT,
    store_and_fwd_flag CHAR(1),
    pulocationid TEXT,
    dolocationid TEXT,
    payment_type INTEGER,
    fare_amount NUMERIC,
    extra NUMERIC,
    mta_tax NUMERIC,
    tip_amount NUMERIC,
    tolls_amount NUMERIC,
    improvement_surcharge NUMERIC,
    total_amount NUMERIC,
    congestion_surcharge NUMERIC,
    airport_fee NUMERIC
);
