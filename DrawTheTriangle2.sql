-- P(R) represents a pattern drawn by Julia in R rows. The following pattern represents P(5):

-- * 
-- * * 
-- * * * 
-- * * * * 
-- * * * * *
-- Write a query to print the pattern P(20).

set @Number = 0;
select repeat('* ', @Number := @Number + 1)
from information_schema.tables
limit 20;

