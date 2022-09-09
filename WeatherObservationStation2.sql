-- Query the following two values from the STATION table:

-- The sum of all values in LAT_N rounded to a scale of  decimal places.
-- The sum of all values in LONG_W rounded to a scale of  decimal places.
-- Input Format

-- The STATION table is described as follows:

CREATE TABLE STATION (
  ID number,
  CITY varchar2(21),
  STATE varchar2,
  LAT_N number,
  LONG_W number
)

SELECT 
    ROUND(SUM(LAT_N), 2), 
    ROUND(SUM(LONG_W), 2)
FROM STATION;