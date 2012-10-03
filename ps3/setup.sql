-- You should not need to edit this file.

CREATE DATABASE moviedb;
USE moviedb;

CREATE TABLE Movie(
    id CHAR(7) PRIMARY KEY, 
    name VARCHAR(64) not null, 
    year YEAR not null,
    rating ENUM('G', 'PG', 'PG-13', 'R', 'NC-17', 'X'),
    runtime INT,
    genre VARCHAR(16),
    earnings_rank INT
);

CREATE TABLE Person(
    id CHAR(7) PRIMARY KEY, 
    name VARCHAR(64) not null,
    dob DATE,	 
    pob VARCHAR(128)
);

CREATE TABLE Actor(
    actor_id CHAR(7), 
    movie_id CHAR(7), 
    PRIMARY KEY(actor_id, movie_id),
    FOREIGN KEY(actor_id) REFERENCES Person(id),
    FOREIGN KEY(movie_id) REFERENCES Movie(id)
);

CREATE TABLE Director(
    director_id CHAR(7), 
    movie_id CHAR(7), 
    PRIMARY KEY(director_id, movie_id),
    FOREIGN KEY(director_id) REFERENCES Person(id),
    FOREIGN KEY(movie_id) REFERENCES Movie(id)
);

CREATE TABLE Oscar(
    movie_id CHAR(7), 
    person_id CHAR(7), 
    type ENUM('BEST-PICTURE', 'BEST-DIRECTOR', 'BEST-ACTRESS',
      'BEST-ACTOR', 'BEST-SUPPORTING-ACTRESS', 'BEST-SUPPORTING-ACTOR'),
    year YEAR,
    PRIMARY KEY(movie_id, type, year),	
    FOREIGN KEY(movie_id) REFERENCES Movie(id),
    FOREIGN KEY(person_id) REFERENCES Person(id)
);

 
LOAD DATA LOCAL INFILE "movie.in" INTO TABLE Movie;
LOAD DATA LOCAL INFILE "person.in"  INTO TABLE Person;
LOAD DATA LOCAL INFILE "actor.in" INTO TABLE Actor;
LOAD DATA LOCAL INFILE "director.in" INTO TABLE Director;
LOAD DATA LOCAL INFILE "oscar.in" INTO TABLE Oscar;
