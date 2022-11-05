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

-- there are multiple Submissions for the same challenge

-- The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of  from your result.

SELECT sc.hacker_id, name, sum(mscore)
FROM (
        SELECT hacker_id, challenge_id 
              , max(score) as mscore
        FROM SUBMISSIONS
        GROUP by hacker_id, challenge_id
        Having max(score) > 0 ) sc
INNER JOIN hackers as ha  ON sc.hacker_id = ha.hacker_id
GROUP BY sc.hacker_id, name
ORDER by sum(mscore) desc, sc.hacker_id;