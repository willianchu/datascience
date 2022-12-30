-- Write a query to print all prime numbers less than or equal to 100. Print your result on a single line, and use the ampersand (&) character as your separator (instead of a space).

SELECT GROUP_CONCAT(NUMB SEPARATOR '&')
FROM (
    SELECT @num:=@num+1 as NUMB FROM -- count 2 to beyond 
    information_schema.tables t1,
    information_schema.tables t2,
    (SELECT @num:=1) tmp
) tempNum
WHERE NUMB<=1000 AND NOT EXISTS(
		SELECT * FROM (
			SELECT @nu:=@nu+1 as NUMA FROM
			    information_schema.tables t1,
			    information_schema.tables t2,
			    (SELECT @nu:=1) tmp1
			    LIMIT 1000
			) tatata
		WHERE FLOOR(NUMB/NUMA)=(NUMB/NUMA) AND NUMA<NUMB AND NUMA>1
	)


-- 2 loops to find prime numbers. The first loop is to count from 2 to 1000. The second loop is to check if the number is prime. If it is, then it will be printed. If not, then it will be ignored. The first loop is to count from 2 to 1000. The second loop is to check if the number is prime. If it is, then it will be printed. If not, then it will be ignored.