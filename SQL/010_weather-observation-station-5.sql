-- Basic Select: Weather Observation Station 5
-- This video helped me understand the issue: https://www.youtube.com/watch?v=13h5BXK8l3g

SELECT CITY, LENGTH(CITY)
FROM (
    SELECT CITY, LENGTH(CITY) FROM STATION
    ORDER BY LENGTH(CITY), CITY
)
LIMIT 1;

SELECT CITY, LENGTH(CITY)
FROM (
    SELECT CITY, LENGTH(CITY) FROM STATION
    ORDER BY LENGTH(CITY) DESC, CITY
)
LIMIT 1;