CREATE TABLE Months_Temperatures (
    TEMPERATURE INTEGER NOT NULL,
    MONTH VARCHAR(9) NOT NULL
);

INSERT INTO Months_Temperatures VALUES (25, 'January');
INSERT INTO Months_Temperatures VALUES (27, 'February');
INSERT INTO Months_Temperatures VALUES (28, 'March');
INSERT INTO Months_Temperatures VALUES (30, 'April');
INSERT INTO Months_Temperatures VALUES (32, 'May');
INSERT INTO Months_Temperatures VALUES (31, 'June');
INSERT INTO Months_Temperatures VALUES (30, 'July');
INSERT INTO Months_Temperatures VALUES (29, 'August');
INSERT INTO Months_Temperatures VALUES (27, 'September');
INSERT INTO Months_Temperatures VALUES (26, 'October');
INSERT INTO Months_Temperatures VALUES (25, 'November');
INSERT INTO Months_Temperatures VALUES (25, 'December');

-- MYSQL
-- Calculate de Median without using the median function

SET @rowindex := -1;
SELECT
   AVG(t.temperature) as Median
FROM
(SELECT @rowindex:=@rowindex + 1 AS rowindex,
        m.temperature AS temperature
        FROM Months_Temperatures m) AS t
WHERE
t.rowindex IN (FLOOR(@rowindex / 2), CEIL(@rowindex / 2));
