-- Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
-- The STATION table is described as follows:
CREATE TABLE STATION (
  ID number,
  CITY varchar2(21),
  STATE varchar2,
  LAT_N number,
  LONG_W number
)

SELECT COUNT(CITY)-COUNT(DISTINCT CITY) AS DIFFERENCE
FROM STATION;