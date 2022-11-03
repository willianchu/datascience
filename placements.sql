CREATE TABLE Students (
    ID INTEGER NOT NULL,
    Name String NOT NULL
);

-- Only the best friend
CREATE TABLE Friends (
    ID INTEGER NOT NULL,
    Friend_ID INTEGER NOT NULL
);

-- Salary is in $ thousands per month
CREATE TABLE Packages (
    ID INTEGER NOT NULL,
    Salary Float NOT NULL
);

SELECT Name
FROM Students
INNER JOIN Friends
ON Students.ID = Friends.ID
INNER JOIN Packages AS StudentPackage
ON Friends.ID = StudentPackage.ID
INNER JOIN Packages AS FriendPackage
ON Friends.Friend_ID = FriendPackage.ID
WHERE StudentPackage.Salary < FriendPackage.Salary
ORDER BY FriendPackage.Salary;
