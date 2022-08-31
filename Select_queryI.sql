-- Query all columns for all American cities in the CITY table with populations larger than 100000. The CountryCode for America is USA.The CITY table is described as follows:
CREATE TABLE City {
  ID  int,
  Name  varchar2(17),
  CountryCode varchar2(3),
  District  varchar2(20),
  Population int  
}

SELECT *
FROM CITY
WHERE POPULATION > 100000 AND COUNTRYCODE = 'USA';

