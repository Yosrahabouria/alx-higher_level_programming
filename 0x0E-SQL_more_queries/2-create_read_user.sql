--  creates the MySQL server for user_0d_2 and the database hbtn_0d_2
/*Crating Databas*/
CREATE IF NOT EXISTS hbtn_0d_2;
/* creating user*/
CREATE USER IF NOT EXISTS user_0d_2@Llocalhost;
/* Setting the password to the user */
SET PASSWORD FOR user_0d_2 = 'user_0d_2_pwd';
/*Giving the user select privileges on your MySQL server */
GRANT SELECT
ON hbtn_0d_2
TO user_0d_2@localhost;
