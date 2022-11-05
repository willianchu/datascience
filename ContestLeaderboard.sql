CREATE TABLE Hackers(
  hacker_id INT NOT NULL,
  name VARCHAR(255)
);

CREATE TABLE Submissions(
  submission_id INT NOT NULL,
  hacker_id INT NOT NULL,
  challenge_id INT NOT NULL,
  score INT NOT NULL
);

SELECT 
    hacker_id, name,
    total_score
FROM
(SELECT 
    h.hacker_id, name,
    SUM(score) AS total_score
FROM
    Hackers h
    INNER JOIN Submissions s
    ON h.hacker_id = s.hacker_id
GROUP BY
    hacker_id, name
ORDER BY
    total_score DESC, hacker_id ASC) AS t
WHERE
    total_score <> 0;

