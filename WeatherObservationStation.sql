-- Consider  and  to be two points on a 2D plane where  are the respective minimum and maximum values of Northern Latitude (LAT_N) and  are the respective minimum and maximum values of Western Longitude (LONG_W) in STATION.

-- Query the Euclidean Distance between points  and  and format your answer to display  decimal digits.

-- Input Format

-- The STATION table is described as follows:

CREATE TABLE STATION (
  ID number,
  CITY varchar2(21),
  STATE varchar2,
  LAT_N number,
  LONG_W number
)

-- distance by Euclidean
SELECT 
    ROUND (
        SQRT(
          POWER( (MAX(LAT_N) - MIN(LAT_N)), 2) + 
          POWER( (MAX(LONG_W) - MIN(LONG_W)), 2)
          ) 
        , 4)
FROM STATION;