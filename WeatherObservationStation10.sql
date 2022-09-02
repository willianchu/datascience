-- Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.

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
WHERE right(CITY, 1) NOT IN ('a','e','i','o','u');