-- Basic Join - Average Population of Each Continent
SELECT COUNTRY.Continent, FLOOR(AVG(CITY.Population))
FROM COUNTRY
INNER JOIN CITY ON COUNTRY.Code = CITY.CountryCode
GROUP BY COUNTRY.Continent;