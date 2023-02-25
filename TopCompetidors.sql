CREATE TABLE  Hackers (
  hacker_id INT NOT NULL,
  name VARCHAR(50) NOT NULL,
)
CREATE TABLE Difficulty (
  difficulty_level INT NOT NULL,
  score INT NOT NULL,
)
CREATE TABLE Challenges (
  challenge_id INT NOT NULL,
  hacker_id INT NOT NULL,
  difficulty_level INT NOT NULL,
  FOREIGN KEY (hacker_id) REFERENCES Hackers(hacker_id),
  FOREIGN KEY (difficulty_level) REFERENCES Difficulty(difficulty_level),
)
CREATE TABLE Submissions (
  submission_id INT NOT NULL,
  hacker_id INT NOT NULL,
  challenge_id INT NOT NULL,
  score INT NOT NULL,
  FOREIGN KEY (hacker_id) REFERENCES Hackers(hacker_id),
  FOREIGN KEY (challenge_id) REFERENCES Challenges(challenge_id),
)
)