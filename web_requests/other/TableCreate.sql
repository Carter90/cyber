use cybercampsql
CREATE TABLE Users (
    UserName varchar(255) NOT NULL PRIMARY KEY,
    HashedPassword binary(64) NOT NULL
);

CREATE TABLE Messages (
    MessageID int NOT NULL PRIMARY KEY,
    UserName varchar(255) NOT NULL,
    Text varchar(255),
    FOREIGN KEY (UserName) REFERENCES Users(UserName)
);

INSERT INTO Users VALUES ('carter', 111111); 
INSERT INTO Messages VALUES (1,'carter', 'Greetings!'); 
