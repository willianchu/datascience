-- P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):
-- *****
-- ****
-- ***
-- **
-- *
-- write a query to print P(20) in MySQL

SET @Number = 21;
SELECT REPEAT('*', @Number := @Number - 1)
FROM INFORMATION_SCHEMA.TABLES
LIMIT 20;


