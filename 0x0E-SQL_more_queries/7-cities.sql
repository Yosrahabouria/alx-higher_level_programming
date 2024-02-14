-- creates the database hbtn_0d_usa
/*Creating Database*/
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

/* create the table cities */
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	PRIMARY KEY (id), 
	id INT AUTO_INCREMENT, 
	state_id INT NOT NULL, 
	name VARCHAR(256), 
	
	FOREIGN KEY (state_id)
	       REFERENCES hbtn_0d_usa.states(id));

