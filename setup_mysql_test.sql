-- prepares a MySQL server for the project
-- database hbnb_test_db
-- new user hbnb_test (in localhost)
-- password of hbnb_test should be set to hbnb_test_pwd
-- hbnb_test with privileges on the database hbnb_test_db (only)
-- hbnb_test with SELECT privilege on the database performance_schema (only)
-- if the database hbnb_test_db or the user hbnb_test already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES
ON
    `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT
SELECT
ON
    `performance_schema`.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
