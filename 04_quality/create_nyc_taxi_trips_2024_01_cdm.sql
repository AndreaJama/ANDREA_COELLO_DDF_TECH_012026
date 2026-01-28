CREATE TABLE nyc_taxi_trips_2024_01_cdm AS
SELECT
    md5(vendorid::text)                          AS vendor_id,
    tpep_pickup_datetime                         AS pickup_datetime,
    tpep_dropoff_datetime                        AS dropoff_datetime,

    EXTRACT(EPOCH FROM 
        (tpep_dropoff_datetime - tpep_pickup_datetime)
    )::INT                                       AS trip_duration_seconds,

    passenger_count::INT                         AS passenger_count,
    trip_distance                                AS trip_distance_miles,

    pulocationid                                 AS pickup_location_id,
    dolocationid                                 AS dropoff_location_id,

    ratecodeid                                   AS rate_code,
    payment_type,

    fare_amount,
    extra                                        AS extra_amount,
    mta_tax                                      AS tax_amount,
    tip_amount,
    tolls_amount,
    improvement_surcharge,
    congestion_surcharge,
    airport_fee,
    total_amount

FROM public.nyc_taxi_trips_2024_01;

-- Verificações rápidas após criar a tabela

SELECT COUNT(*) FROM nyc_taxi_trips_2024_01_cdm;

SELECT * FROM nyc_taxi_trips_2024_01_cdm LIMIT 5;
