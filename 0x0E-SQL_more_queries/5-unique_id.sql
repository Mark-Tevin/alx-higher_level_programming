-- creates the table unique_id
-- If the table unique_id already exists, your script should not fail
-- id INT with the default value 1 and must be unique
-- name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
