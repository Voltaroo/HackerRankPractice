-- Aggregation - Weather Observation Station 13
SELECT ROUND(SUM(LAT_N),4)
FROM STATION
WHERE LAT_N BETWEEN 38.788 AND 137.2345;