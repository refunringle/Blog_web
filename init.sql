-- DROP TABLE IF EXISTS Post_Comment CASCADE;


CREATE TABLE [IF NOT EXISTS] user(
    id serial PRIMARY KEY,
	name VARCHAR ( 50 ) UNIQUE NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	password VARCHAR ( 50 ) NOT NULL,
	-- created_on TIMESTAMP NOT NULL,
    -- last_login TIMESTAMP
);

CREATE TABLE [IF NOT EXISTS] post(
    id SERIAL PRIMARY KEY,
    user_id int FORIEGN KEY REFERENCE user(id),
    title VARCHAR(150),
    category VARCHAR(100),
    -- summary TEXT,
    content TEXT, 
    publish_time TIMESTAMP NOT NULL VALUES(default now()),
    -- tag SERIAL 
);

CREATE TABLE [IF NOT EXISTS] Post_Comment(
    id SERIAL ,
    post_id INT FORIEGN KEY REFERENCE post(id),
    Guest_name VARCHAR(100),
    publish_Time TIMESTAMP NOT NULL VALUES(now()),
    comment TEXT
);

CREATE TABLE [IF NOT EXISTS] guest_user(
    id SERIAL PRIMARY KEY,
    post_id INT FORIEGN KEY REFERENCE post(id),
    Guest_name VARCHAR(100),
    GUEST_Time TIMESTAMP NOT NULL VALUES(now()),
    comment TEXT

);