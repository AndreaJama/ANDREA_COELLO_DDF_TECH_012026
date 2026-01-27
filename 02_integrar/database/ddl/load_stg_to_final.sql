INSERT INTO public.nyc_taxi_trips_2024_01
SELECT
    CAST(vendorid AS INTEGER),
    TO_TIMESTAMP(tpep_pickup_datetime, 'YYYY-MM-DD HH24:MI:SS'),
    TO_TIMESTAMP(tpep_dropoff_datetime, 'YYYY-MM-DD HH24:MI:SS'),
    CAST(passenger_count AS INTEGER),
    trip_distance,
    CAST(ratecodeid AS INTEGER),
    store_and_fwd_flag,
    CAST(pulocationid AS INTEGER),
    CAST(dolocationid AS INTEGER),
    payment_type,
    fare_amount,
    extra,
    mta_tax,
    tip_amount,
    tolls_amount,
    improvement_surcharge,
    total_amount,
    congestion_surcharge,
    airport_fee
FROM public.nyc_taxi_trips_2024_01_stg;

-- Validação
SELECT COUNT(*) FROM public.nyc_taxi_trips_2024_01;
