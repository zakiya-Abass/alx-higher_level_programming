-- Creates hbtn_0d_2 database and user_0d_2 user
-- user_0d_2 has only SELECT privileges in hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
	IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
	ON hbtn_0d_2.*
	TO 'user_0d_2'@'localhost';
