-- Basic Select - Weather Observation Station 12

SELECT DISTINCT CITY FROM STATION
WHERE LOWER(LEFT(CITY, 1)) NOT IN ('a','e','i','o','u')
  AND LOWER(RIGHT(CITY,1)) NOT IN ('a','e','i','o','u');