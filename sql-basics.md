-- 1. Create a users table using security best practices
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    -- Using 255 length to accommodate hashed passwords (e.g., Bcrypt/Argon2)
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Inserting data (Simulating hashed passwords instead of plain text)
INSERT INTO users (username, password_hash) 
VALUES ('admin', '$2b$12$ExmpleHashValueReflectingBestPractices');

-- 3. Secure Querying (Prevention of SQL Injection)
-- Instead of concatenating inputs, we use Prepared Statements
PREPARE login_stmt FROM 'SELECT id, username FROM users WHERE username = ? AND password_hash = ?';

-- Simulating user inputs
SET @user_input = 'admin';
SET @pass_input = '$2b$12$ExmpleHashValueReflectingBestPractices';

-- Executing the query safely
EXECUTE login_stmt USING @user_input, @pass_input;

-- Clean up
DEALLOCATE PREPARE login_stmt;
