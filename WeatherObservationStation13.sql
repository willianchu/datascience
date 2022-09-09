-- Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than  38.7880 and less than 137.2345 . Truncate your answer to 4 decimal places.

-- Input Format

-- The STATION table is described as follows:

CREATE TABLE STATION (
  ID number,
  CITY varchar2(21),
  STATE varchar2,
  LAT_N number,
  LONG_W number
)

SELECT TRUNCATE(SUM(LAT_N), 4)
FROM STATION
WHERE LAT_N > 38.7880 AND LAT_N < 137.2345