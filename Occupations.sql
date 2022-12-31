-- Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.
-- Note: Print NULL when there are no more names corresponding to an occupation.

-- Input Format

-- The OCCUPATIONS table is described as follows:

CREATE TABLE IF NOT EXISTS OCCUPATIONS(
    NAME VARCHAR(20)
    OCCUPATION VARCHAR(20),
);

-- Occupation will only contain one of the following values: Doctor, Professor, Singer or Actor.
-- order by values Doctor, Professor, Singer, Actor

SELECT *
FROM (  SELECT NAME, OCCUPATION
        FROM OCCUPATIONS
        WHERE OCCUPATION = 'Doctor' OR OCCUPATION = 'Professor' OR OCCUPATION = 'Singer'
        ORDER BY OCCUPATION) AS FIRST_THREE
UNION
SELECT *
FROM (SELECT NAME, OCCUPATION
FROM OCCUPATIONS
WHERE OCCUPATION = 'Actor'
ORDER BY OCCUPATION, NAME) AS LAST_ONE;



