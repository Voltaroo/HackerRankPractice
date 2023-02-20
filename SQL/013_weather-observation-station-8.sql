-- Basic Select - Weather Observation Station 8

SELECT DISTINCT CITY FROM STATION
WHERE LOWER(LEFT(CITY, 1)) IN ('a','e','i','o','u')
  AND LOWER(RIGHT(CITY,1)) IN ('a','e','i','o','u');

-- Apparently, this work as well: SELECT DISTINCT CITY FROM STATION WHERE CITY LIKE '[aeiou]%[aeiou]'; 