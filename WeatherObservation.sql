-- Query a list of CITY and STATE from the STATION table.
-- The STATION table is described as follows:
CREATE TABLE STATION (
  ID number,
  CITY varchar2(21),
  STATE varchar2,
  LAT_N number,
  LONG_W number
)

SELECT CITY, STATE
FROM STATION;