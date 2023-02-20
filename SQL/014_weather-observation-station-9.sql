-- Basic Select - Weather Observation Station 9

SELECT DISTINCT CITY FROM STATION
WHERE LOWER(LEFT(CITY,1)) NOT IN ('a','e','i','o','u');