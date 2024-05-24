-- creates the database hbtn_0d_usa and the table states
-- If the database hbtn_0d_usa already exists, script should not fail
-- If the table states already exists, script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa

-- Switch to the database btn_0d_usa
USE btn_0d_usa;

-- Create the table states if it does not exist
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
