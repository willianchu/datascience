-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

-- Input Format

-- The STATION table is described as follows:
CREATE TABLE STATION (
  ID number,
  CITY varchar2(21),
  STATE varchar2,
  LAT_N number,
  LONG_W number
)

SELECT DISTINCT CITY
FROM STATION
WHERE LEFT(CITY, 1) IN ( 'A','E','I','O', 'U')

-- LEFT(name , 1) IN ('a','e','i','o','u')
-- RIGHT(name,1) IN  ('a','e','i','o','u')

-- select DISTINCT city from station where city REGEXP '^[aeiou]';