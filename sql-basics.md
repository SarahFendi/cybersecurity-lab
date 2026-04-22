# SQL Basics – Sarah

## Creating a Table
```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);
INSERT INTO users VALUES (1, 'admin', '1234');
INSERT INTO users VALUES (2, 'user', 'password');
SELECT * FROM users;
SELECT * FROM users 
WHERE username = 'admin' AND password = '1234';
