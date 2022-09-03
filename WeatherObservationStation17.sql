-- Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is 38.7780 greater than . Round your answer to 4 decimal places.

-- Input Format

-- The STATION table is described as follows:
CREATE TABLE STATION (
  ID number,
  CITY varchar2(21),
  STATE varchar2,
  LAT_N number,
  LONG_W number
)
SELECT CAST(ROUND(LONG_W, 4) AS DECIMAL(10,4))
FROM STATION
WHERE CAST(ROUND(LAT_N, 4) AS DECIMAL(10,4)) > 33.7780


SELECT ROUND(long_w,4) FROM station WHERE lat_n = (SELECT MIN(lat_n) FROM station WHERE lat_n > 38.7780);

38.85256239