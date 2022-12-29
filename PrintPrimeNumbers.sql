-- Write a query to print all prime numbers less than or equal to 100. Print your result on a single line, and use the ampersand (&) character as your separator (instead of a space).

-- WITH RECURSIVE cte (Number) AS (
--     SELECT 1            -- base case returns 1
--     UNION ALL
--     SELECT Number + 1   -- recursive case returns 1 + previous value
--     FROM cte
--     WHERE Number < 100
-- )

-- SELECT concat("&",Number) 
-- FROM cte
-- where ((Number * Number ) / (Number - 1)) <> 0
-- ORDER BY Number;

with x(val) as (select 1 val from dual 
                union all 
                select val+1 from x where val < 100)
,primes as 
(select val
from (                
select x.val,x1.val as divisor,mod(x.val,x1.val)  as remaindr
from x
join x x1 on x1.val <= x.val)
group by val
having sum(case when remaindr = 0 then 1 else 0 end) = 2
)
select * from primes
