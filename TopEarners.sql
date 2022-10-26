CREATE TABLE Employee (
    employee_id int NOT NULL,
    Name varchar(255) NOT NULL,
    months int NOT NULL,
    salary int NOT NULL
);

SELECT salary * months AS earnings, count(*) AS num_employees
FROM Employee
WHERE earnings = (SELECT MAX(salary * months) FROM Employee)
GROUP BY earnings
ORDER BY earnings DESC;


