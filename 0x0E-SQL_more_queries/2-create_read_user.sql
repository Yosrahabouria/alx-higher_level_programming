--  creates the MySQL server for user_0d_2 and the database hbtn_0d_2
/* Crating Database */
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

/* creating user */
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

/* Setting the password to the user */
/*SET PASSWORD FOR user_0d_2@localhost = 'user_0d_2_pwd';*/

/* Giving the user select privileges on your MySQL server */
GRANT SELECT
 ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
