# =====================================================
# SQL INJECTION SECURITY LAB (FULL VERSION)
# Vulnerable → Attack → Secure Fix
# =====================================================


# =====================================================
# 1. VULNERABLE VERSION (REAL-WORLD EXAMPLE)
# =====================================================

-- ❌ BAD PRACTICE: Direct input concatenation (SQL Injection risk)

-- Example login query (vulnerable backend logic)
-- Imagine this is constructed in PHP/Python/Node.js:

-- SELECT id, username
-- FROM users
-- WHERE username = '" + user_input + "'
-- AND password = '" + pass_input + "';

-- =====================================================
-- 🔥 ATTACK SCENARIO
-- =====================================================

-- Attacker input:
-- username: ' OR '1'='1
-- password: anything

-- Resulting injected query:

SELECT id, username
FROM users
WHERE username = '' OR '1'='1'
AND password = 'anything';

-- 💣 RESULT:
-- Authentication bypass (returns all users or first match)


# =====================================================
# 2. SECURE DATABASE SCHEMA
# =====================================================

CREATE TABLE users (
id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(50) NOT NULL UNIQUE,

-- Never store plain passwords
password_hash VARCHAR(255) NOT NULL,

created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


# =====================================================
# 3. SECURE DATA INSERTION
# =====================================================

-- Passwords must be hashed in application layer (bcrypt / argon2)

INSERT INTO users (username, password_hash)
VALUES ('admin', '$2b$12$ExmpleHashValueReflectingBestPractices');


# =====================================================
# 4. SECURE LOGIN (FIXED VERSION)
# =====================================================

-- ✔️ Only fetch data using safe parameterized query

PREPARE login_stmt FROM '
SELECT id, username, password_hash
FROM users
WHERE username = ?
';

SET @user_input = 'admin';

EXECUTE login_stmt USING @user_input;

DEALLOCATE PREPARE login_stmt;


# =====================================================
# 5. APPLICATION-LEVEL PASSWORD CHECK (IMPORTANT)
# =====================================================

-- SQL is NOT responsible for password verification

-- Example (Python logic):

"""
import bcrypt

stored_hash = get_password_hash_from_db(username)

if bcrypt.checkpw(input_password, stored_hash):
print("Login success")
else:
print("Login failed")
"""


# =====================================================
# 6. SECURITY IMPROVEMENTS SUMMARY
# =====================================================

-- ❌ Vulnerable:
-- String concatenation in SQL → SQL Injection possible

-- ✅ Fixed:
-- Prepared Statements → input treated as data only

-- ❌ Wrong approach:
-- Password comparison inside SQL

-- ✅ Correct approach:
-- Password verification in application layer using bcrypt/argon2

-- ❌ Plain passwords:
-- NEVER store passwords in plain text

-- ✅ Secure storage:
-- Always store hashed passwords only


# =====================================================
# 7. WHAT THIS LAB DEMONSTRATES
# =====================================================

-- 1. How SQL Injection works in real systems
-- 2. How attackers bypass authentication
-- 3. How Prepared Statements prevent injection
-- 4. Why password hashing is mandatory
-- 5. Proper secure authentication architecture
