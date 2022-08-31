-- Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.

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
WHERE COUNTRYCODE = 'JPN';