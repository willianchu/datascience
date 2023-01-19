-- #05 Consider the follolwing data table named Student

CREATE TABLE Student
(
    StudentName varchar(50),
    NumberID int,
    Sex varchar(1),
)

INSERT INTO Student VALUES('Ben',3412,'M')
INSERT INTO Student VALUES('Dan',1234,'M')
INSERT INTO Student VALUES('Nel',2341,'F')

-- Whats the count of rows returned in the following relational seletion?
-- σ(Number<3000)(Student)

SELECT COUNT(*)
FROM Student 
WHERE NumberID < 3000;

--  answer: 2

-- #6 erase all data in Student table
DELETE * FROM Student;
INSERT INTO Student VALUES('Nina',3412,'F')
INSERT INTO Student VALUES('Mike',1234,'M')
INSERT INTO Student VALUES('Nelson',2341,'F')

-- What is the count of attributes (columns) returned in the following projection?
-- π(Name, Number)(Student)

-- return the number of columns in the table Name and Number
SELECT COUNT(*) as No_Of_Columns
FROM 
(
    SELECT StudentName, NumberID
    FROM Student
) AS StudentNameAndNumber;
-- answer: 2

-- NOTE:
-- π - project operation
-- Used to retrieve columns

-- σ - select operation
-- Used to retrieve rows

-- π(Name, Number)(Student) hence this will return all data in name and number columns.

