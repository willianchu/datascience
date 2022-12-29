-- Write a query to print all prime numbers less than or equal to 100. Print your result on a single line, and use the ampersand (&) character as your separator (instead of a space).

Create Procedure PrintPrimeNumbers
@startnum int,
@endnum int
AS 
BEGIN
Declare @a INT;
Declare @i INT = 1
(
Select a = @startnum / 2;
WHILE @i<@a
BEGIN
@startnum%(@a-@i)
i=i+1;
)
END



