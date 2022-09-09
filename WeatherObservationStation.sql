<!-- Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than . Round your answer to  decimal places.

Input Format

The STATION table is described as follows: -->

CREATE TABLE STATION (
  ID number,
  CITY varchar2(21),
  STATE varchar2,
  LAT_N number,
  LONG_W number
)

SET @MAX_LAT = (SELECT MAX(LAT_N)
FROM STATION
WHERE LAT_N < 137.2345);

SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N = @MAX_LAT;

-- REFACTORED

SELECT ROUND(LONG_W, 4)
FROM STATION
WHERE LAT_N < 137.2345
ORDER BY LAT_N DESC LIMIT 1;

