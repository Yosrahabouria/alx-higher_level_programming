-- creates the database hbtn_0d_usa 
/*Creating Database*/
CREATE IF NOT EXISTS hbtn_0d_usa;
/* create the table states */
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	PRIMARY KEY id,
	id INT AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL);
