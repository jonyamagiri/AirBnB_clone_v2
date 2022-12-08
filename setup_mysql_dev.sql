-- prepares a MySQL server for the project
-- database hbnb_dev_db
-- new user hbnb_dev (in localhost) with all privileges on the database hbnb_dev_db 
-- password of hbnb_dev set to hbnb_dev_pwd
-- hbnb_dev with SELECT privilege on the database performance_schema (only)
-- if the database hbnb_dev_db or the user hbnb_dev already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbnb_dev_db; 
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd'; 
GRANT ALL PRIVILEGES
ON
    `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT
SELECT
ON
    `performance_schema`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
