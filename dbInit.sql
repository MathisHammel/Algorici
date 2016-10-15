CREATE TABLE Users
(
id INTEGER,
nickname TEXT,
hashedPass TEXT,
pwdSalt TEXT,
name TEXT,
firstName TEXT,
promo INTEGER,
submitInQueue INTEGER,
isAdmin INTEGER
PRIMARY KEY(id)
);

CREATE TABLE Problems
(
id INTEGER,
userId INTEGER,
maxScore REAL,
FOREIGN KEY(userId) REFERENCES Users(id),
PRIMARY KEY(id,userId)
);

CREATE TABLE Submissions
(
id INTEGER,
userId INTEGER,
problemId INTEGER,
score REAL,
PRIMARY KEY(id),
FOREIGN KEY(userId) REFERENCES Users(id),
FOREIGN KEY(problemId) REFERENCES Problems(id)
);
