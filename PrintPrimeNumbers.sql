-- Write a query to print all prime numbers less than or equal to 100. Print your result on a single line, and use the ampersand (&) character as your separator (instead of a space).

WITH RECURSIVE cte (Number) AS (
    SELECT 1            -- base case returns 1
    UNION ALL
    SELECT Number + 1   -- recursive case returns 1 + previous value
    FROM cte
    WHERE Number < 100
)

SELECT concat("&",Number) 
FROM cte
where ((Number * Number ) / (Number - 1)) <> 0
ORDER BY Number;


