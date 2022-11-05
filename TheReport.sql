-- You are given two tables: Students and Grades. Students contains three columns ID, Name and Marks.

CREATE TABLE Students (ID INTEGER, Name TEXT, Marks INTEGER);
CREATE TABLE Grades (ID INTEGER, Min_Mark INTEGER, Max_Mark INTEGER);

--  generate a report containing three columns: Name, Grade and Mark. 
-- we doesn't want the NAMES of those students who received a grade lower than 8.
-- The report must be in descending order by grade 
-- If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically.
-- If the grade is lower than 8, use "NULL" as their name and list them by their marks in descending order.
-- If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

SELECT 
  Name, 
  (SELECT Grade FROM Grades WHERE s.Marks >= Min_Mark AND s.Marks <= Max_Mark) AS Grade,
  Marks
FROM
  Students s;

