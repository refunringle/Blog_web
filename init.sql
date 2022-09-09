DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS Post CASCADE;
DROP TABLE IF EXISTS Post_Comment CASCADE;
DROP TABLE IF EXISTS guest_user CASCADE;

    -- MY DATA BASE NAME IS blog **

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
	name VARCHAR (50) UNIQUE NOT NULL,
	email VARCHAR (255) UNIQUE NOT NULL,
	password VARCHAR (50) NOT NULL
	-- created_on TIMESTAMP NOT NULL,
    -- last_login TIMESTAMP
);

CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    user_id INT references users(id),
    title VARCHAR(150),
    category VARCHAR(100),
    -- summary TEXT,
    content TEXT, 
    publish_time TIMESTAMP NOT NULL
    -- tag SERIAL  
);

CREATE TABLE Post_Comment (
    id SERIAL PRIMARY KEY,
    post_id INT references post(id),
    Guest_name VARCHAR(100),
    publish_Time TIMESTAMP NOT NULL ,
    comment TEXT
);

CREATE TABLE guest_user(
    id SERIAL PRIMARY KEY,
    post_id INT references Post_Comment(id),
    Guest_name VARCHAR(100),
    GUEST_Time TIMESTAMP NOT NULL ,
    comment TEXT
);
