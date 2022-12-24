create database for_education;
show databases;
use for_education;
CREATE TABLE persons (
	id int,
    name varchar(255),
    age int,
    address varchar(255),
    PRIMARY KEY (id)
);
CREATE TABLE students (
	id int,
    name varchar(255),
    age int,
    examen1 int,
    examen2 int,
    examen3 int,
    average float,
    scholarship varchar(255),
    PRIMARY KEY (id)
);
CREATE TABLE collaborators (
	id int,
    position_ varchar(255),
    salary int,
    social_security int,
    age int,
    address_ varchar(255),
    PRIMARY KEY (id)
);
-- INSERT INTO persons (name, age, address) VALUES ("Juan", 35, "calle falsa 123");
-- Esta linea no sera ejecutada

ALTER TABLE persons MODIFY COLUMN id int auto_increment;

SHOW CREATE TABLE persons;

CREATE TABLE `persons` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO persons (name, age, address) VALUES ("Rodrigo", 33, "una calle hay numero algo");
INSERT INTO persons (name, age, address) VALUES ("Ana", 28, "calle 13");
INSERT INTO persons (name, age, address) VALUES ("Lorine", 25, "zona colonial");
INSERT INTO persons (name, age, address) VALUES ("Daneyris", 30, "kings Landing");

SELECT * FROM persons;
