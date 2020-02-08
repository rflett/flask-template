DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username varchar(80) UNIQUE NOT NULL,
    email varchar(120) UNIQUE NOT NULL,
    age integer DEFAULT NULL,
    city varchar(3) DEFAULT NULL
);
