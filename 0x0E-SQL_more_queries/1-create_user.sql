--  creates the MySQL server user user_0d_1
/* creating user*/
CREATE USER IF NOT EXISTS user_0d_1@localhost;
/* Setting the password to the user */
SET PASSWORD FOR user_0d_1@localhost = 'user_0d_1_pwd';
/*Giving the user all privileges on your MySQL server */
GRANT ALL PRIVILEGES
ON *.*
TO user_0d_1@localhost;
FLUSH PRIVILEGES;
