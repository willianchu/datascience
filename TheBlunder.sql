-- Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's 0 key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

-- Write a query calculating the amount of error (i.e.: miscalculated - average monthly salaries), and round it up to the next integer.

-- Input Format

-- The EMPLOYEES table is described as follows:

CREATE TABLE EMPLOYEES (
  ID  Intehger,
  Name  String,
  Salary  Integer,
)
SELECT CEIL(AVG(Salary)-AVG(REPLACE(Salary, '0', '')))
FROM EMPLOYEES
