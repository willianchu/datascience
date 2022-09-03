-- Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. Output one of the following statements for each record in the table:

-- Equilateral: It's a triangle with  sides of equal length.
-- Isosceles: It's a triangle with  sides of equal length.
-- Scalene: It's a triangle with  sides of differing lengths.
-- Not A Triangle: The given values of A, B, and C don't form a triangle.
-- Input Format

-- The TRIANGLES table is described as follows:

CREATE TABLE TRIANGLES (
  A Integer,
  B Integer,
  C Integer,
)

SELECT
    IF (A >= B+C OR B >= A+C OR C >= A+B, "Not A Triangle",
      IF (A=B AND B=C, "Equilateral", 
        IF (A=B OR B=C OR C=A, "Isosceles",
               "Scalene"
    )))
FROM TRIANGLES;

SELECT
    CASE
        WHEN A + B <= C OR B + C <= A OR  A + C <= B THEN "Not A Triangle"
        WHEN A = B AND A = C THEN "Equilateral"
        WHEN A = B OR A = C OR B = C THEN "Isosceles"     
        ELSE "Scalene"
    END
FROM TRIANGLES








10 10 10 Equilateral
11 11 11 Equilateral
30 32 30 Isosceles
40 40 40 Equilateral
20 20 21 Isosceles
21 21 21 Equilateral
20 22 21 Scalene
20 20 40 Isosceles
20 22 21 Scalene
30 32 41 Scalene
50 22 51 Scalene
20 12 61 Not A Triangle
20 22 50 Not A Triangle
50 52 51 Scalene
80 80 80 Equilateral