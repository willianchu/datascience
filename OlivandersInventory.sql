CREATE TABLE Wands (
  id INT NOT NULL,
  code INT NOT NULL,
  coins_needed INT NOT NULL,
  power INT NOT NULL,
  PRIMARY KEY (id),
)
CREATE TABLE Wands_Property (
  code INT NOT NULL,
  age INT NOT NULL,
  is_evil INT NOT NULL,
  FOREIGN KEY (code) REFERENCES Wands(code),
)