-- Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.
-- Note: Print NULL when there are no more names corresponding to an occupation.

-- Input Format

-- The OCCUPATIONS table is described AS follows:

CREATE TABLE IF NOT EXISTS OCCUPATIONS(
    NAME VARCHAR(20)
    OCCUPATION VARCHAR(20),
);

-- Occupation will only contain one of the following values: Doctor, Professor, Singer or Actor.
-- ORDER BY values Doctor, Professor, Singer, Actor

-- ms sql server
-- SELECT [Doctor], [Professor], [Singer], [Actor]
-- FROM(
--     SELECT ROW_NUMBER() 
--     OVER(
--       PARTITION BY OCCUPATION
--       ORDER BY NAME) AS RN, NAME, OCCUPATION
--     FROM OCCUPATIONS
--     GROUP BY OCCUPATION, NAME) AS TABLE1
-- PIVOT(
--     MAX(NAME)
--     FOR OCCUPATION IN ([Doctor], [Professor], [Singer], [Actor])) AS TABLE2
-- ORDER BY RN;

-- mysql

SELECT doc, prof, singer, act FROM ((
    (SELECT name AS prof,@row_number2:=@row_number2+1 AS id FROM Occupations, (SELECT @row_number2:=0) AS t WHERE Occupation = 'Professor' ORDER BY name) AS TABLE1
LEFT JOIN 
    (SELECT name AS doc,@row_number:=@row_number+1 AS id FROM Occupations, (SELECT @row_number:=0) AS t WHERE Occupation = 'Doctor' ORDER BY name) AS TABLE2 ON TABLE1.id = TABLE2.id)
LEFT JOIN 
(SELECT name AS singer,@row_number3:=@row_number3+1 AS id FROM Occupations, (SELECT @row_number3:=0) AS t WHERE Occupation = 'Singer' ORDER BY name) AS TABLE3 ON TABLE1.id = TABLE3.id)
LEFT JOIN 
(SELECT name AS act,@row_number4:=@row_number4+1 AS id FROM Occupations, (SELECT @row_number4:=0) AS t WHERE Occupation = 'Actor' ORDER BY name) AS TABLE4 ON TABLE1.id = TABLE4.id;



