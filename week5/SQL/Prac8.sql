-- CREATE TABLE team(
-- id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
-- teamName VARCHAR(255)
-- )

CREATE TABLE score(
id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
teamid INT,
userid INT,
score INT,
FOREIGN KEY (teamid) REFERENCES team(id),
FOREIGN KEY (userid) REFERENCES `user`(id)
)