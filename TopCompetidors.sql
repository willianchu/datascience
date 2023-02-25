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

INSERT INTO Hackers VALUES (
  5580, 'Rose',
  8439, 'Angela',
  27205, 'Frank',
  52243, 'Patrick',
  52348, 'Lisa',
  57645, 'Kimberly',
  77726, 'Bonnie',
  83082, 'Michael',
  86870, 'Todd',
  90411, 'Joe',
)
INSERT INTO Difficulty VALUES (
  1, 20,
  2, 30,
  3, 40,
  4, 60,
  5, 80,
  6, 100,
  7, 120,
)
INSERT INTO Challenges (
  4810, 77726, 4,
  21089, 27205, 1,
  36566, 5580, 7,
  66730, 52243, 6,
  71055, 52243, 2,
)
INSERT INTO Submissions (
  68628,77726,36566,30,
  65300,77726,21089,10,
  40326,52243,36566,77,
  8941,27205,4810,4,
  83554,77726,66730,30,
  43353,52243,66730,0,
  55385,52348,71055,20,
  39784,24205,71055,23,
  94613,86870,71055,30,
  45788,52348,36566,0,
  93058,86870,36566,30,
  7344,8439,66730,92,
  2721,8439,4810,36,
  523,5580,71055,4,
  49105,52348,66730,0,
  55877,57645,66730,80,
  38355,27205,66730,35,
  3924,8439,36566,80,
  97397,90411,66730,100,
  74162,83082,4810,40,
  97431,90411,71055,30,
)




SELECT hacker_id, name, SUM(score) AS total_score