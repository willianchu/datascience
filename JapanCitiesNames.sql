-- Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
-- The CITY table is described as follows:

CREATE TABLE City {
  ID  int,
  Name  varchar2(17),
  CountryCode varchar2(3),
  District  varchar2(20),
  Population int  
}

SELECT NAME
FROM CITY
WHERE COUNTRYCODE = 'JPN';