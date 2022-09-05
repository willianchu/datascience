-- Query a count of the number of cities in CITY having a Population larger than .

-- Input Format

-- The CITY table is described as follows:

CREATE TABLE CITY (
  ID  NUMBER,
  NAME  VARCHAR2(17),
  COUNTRYCODE VARCHAR2(3),
  DISTRICT  VARCHAR2(20),
  POPULATION NUMBER,
)

SELECT DISTINCT COUNT(NAME)
FROM CITY
WHERE POPULATION > 100000;

