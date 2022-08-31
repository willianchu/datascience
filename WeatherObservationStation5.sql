-- Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths (i.e.: number of characters in the name). If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.
-- The STATION table is described as follows:
CREATE TABLE STATION (
  ID number,
  CITY varchar2(21),
  STATE varchar2,
  LAT_N number,
  LONG_W number
)

(SELECT CITY, length(city) FROM STATION
WHERE length(CITY) = (SELECT max(length(CITY)) FROM STATION) ORDER BY CITY LIMIT 1)

UNION

(SELECT CITY, length(city) FROM STATION
WHERE length(CITY) = (SELECT min(length(CITY)) FROM STATION)
ORDER BY CITY LIMIT 1);


-- QUERY 2

WITH SMALL AS (
    select CITY, LENGTH(CITY) AS SIZ
    from station
    ORDER BY SIZ, CITY
    LIMIT 1
), BIG AS (
    select CITY, LENGTH(CITY) AS SIZ
    from station
    ORDER BY SIZ, CITY DESC
    LIMIT 1
)
SELECT CITY, SIZ FROM SMALL
UNION
SELECT CITY, SIZ FROM BIG
