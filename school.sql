

DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS teachers;

CREATE TABLE student (
    id  serial PRIMARY KEY,
    first_name  VARCHAR(25) NOT NULL,
    last_name   VARCHAR(25) NOT NULL,
    age     INTEGER NOT NULL,
    subject     int references subjects(id)

);


CREATE TABLE teachers (
    id  serial PRIMARY KEY,
    first_name  VARCHAR(25) NOT NULL,
    last_name   VARCHAR(25) NOT NULL,
    age     INTEGER NOT NULL,
    subject     int references subjects(id)

);

CREATE TABLE subjects (
    id  serial PRIMARY KEY,
    subject     varchar(50)
)

