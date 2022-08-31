-- Query all columns (attributes) for every row in the CITY table.

-- The CITY table is described as follows:
CREATE TABLE City {
  ID  int,
  Name  varchar2(17),
  CountryCode varchar2(3),
  District  varchar2(20),
  Population int  
}

SELECT *
FROM CITY;