-- MySQL setup for test environment
-- A script that prepares a MySQL server for the project

-- create new db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create a user in the localhost
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- grant all privileges to the created user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- grant only read privilege on db 'performance_schema' to the created user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Let all modifications take effect immediately
FLUSH PRIVILEGES;
