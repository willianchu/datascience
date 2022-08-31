-- Query all columns for a city in CITY with the ID 1661.

-- The CITY table is described as follows:
CREATE TABLE City {
  ID  int,
  Name  varchar2(17),
  CountryCode varchar2(3),
  District  varchar2(20),
  Population int  
}

SELECT *
FROM CITY
WHERE ID = 1661;