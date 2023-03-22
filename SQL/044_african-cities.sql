-- Basic Join - African Cities
SELECT CITY.Name
FROM CITY
INNER JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
WHERE COUNTRY.Continent = 'Africa';