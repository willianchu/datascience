CREATE TABLE Hackers
(
    hacker_id int NOT NULL,
    name varchar(50) NOT NULL,
    PRIMARY KEY (hacker_id)
);

CREATE TABLE Submissions
(
    submission_date date NOT NULL,
    submission_id int NOT NULL,
    hacker_id int NOT NULL,
    score int NOT NULL,
    PRIMARY KEY (submissions_id),
    FOREIGN KEY (hacker_id) REFERENCES Hackers(hacker_id)
);

SELECT submission_date, COUNT(DISTINCT Submissions.hacker_id) AS unique_hackers, Hackers.name
FROM Submissions
INNER JOIN Hackers
ON Submissions.hacker_id = Hackers.hacker_id
WHERE submission_date >= '2016-03-01' AND submission_date <= '2016-03-15'
GROUP BY submission_date, Hackers.name;
