-- MySQL development setup
-- A script that prepares a MySQL server for the project

-- create new db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create a user in the localhost
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- grant all privileges to the created user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- grant only read privilege to the created user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Let all modifications take effect immediately
FLUSH PRIVILEGES;
