create database Employees;
show databases; --
use for_education;
show tables;
select * from collaborators;
select * from persons;

-- Modificar 
ALTER TABLE collaborators MODIFY COLUMN id int auto_increment;
ALTER TABLE collaborators MODIFY COLUMN working_hours int;
alter table collaborators modify column social_security varchar(255) after age;

-- Agregar
ALTER TABLE collaborators ADD working_hours varchar(255) AFTER address_;
ALTER TABLE collaborators ADD name varchar(255) AFTER id;
ALTER TABLE collaborators ADD after_name VARCHAR(255) AFTER name;


-- Cambiar
ALTER TABLE collaborators CHANGE nombre name varchar(255);
ALTER TABLE collaborators CHANGE nombre name varchar(255);
SELECT id, nombre AS name FROM collaborators;

-- Borrar
ALTER TABLE collaborators drop column social_security;
ALTER TABLE collaborators drop column address


insert into collaborators (name, after_name, position, salary, age, social_security, address_) values ("Ransel", "Melenciano", "Analista de Datos", 5000, 29,"20185542", "calle no te importa");

insert into collaborators (name, after_name, position_, salary, age, address_,working_hours) VALUES ("Ransel", "Melenciano", "Analista de Datos", 5000, 27,"calle no te importa", 48);
insert into collaborators (name, after_name, position_, salary, age, address_,working_hours) VALUES("Juan", "Molina", "Programador", 1500, 26,"calle villa juana", 48);
insert into collaborators (name, after_name, position_, salary, age, address_,working_hours) VALUES ("Ana", "Fernandez", "Analista de Datos", 2000, 27, "Charles de Gaulle", 40);
insert into collaborators (name, after_name, position_, salary, age, address_,working_hours) VALUES ("Pedro", "Morrinson", "Jefe de proyecto", 2500, 30, "Cancino", 42); 
insert into collaborators (name, after_name, position_, salary, age, address_,working_hours) VALUES ("Sofía", "Martinez", "Gerente de TI", 3000, 28, "Residencial las Acacias", 50);
insert into collaborators (id, working_hours) values (1, 47);

-- Error Code: 1064. You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'insert into collaborators (name, after_name, position_, salary, age, address_,wo' at line 2


SELECT name FROM persons WHERE id = 1;
SELECT * FROM persons WHERE age = 28 AND name = "Ana";

-- Cambio:
UPDATE persons SET age = 30 WHERE id = 1;
UPDATE collaborators SET working_hours = 40 WHERE id = 1;
UPDATE collaborators SET working_hours = 42 WHERE id = 2;
UPDATE collaborators SET working_hours = 48 WHERE id = 3;
UPDATE collaborators SET working_hours = 48 WHERE id = 4;
UPDATE collaborators SET working_hours = 40 WHERE id = 5;
UPDATE collaborators SET working_hours = 40 WHERE id = 1;

delete from collaborators where id = 6;


SHOW CREATE TABLE collaborators;
CREATE TABLE `collaborators` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `after_name` varchar(255) DEFAULT NULL,
  `position` varchar(255) DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `age` int DEFAULT NULL,
  `working_hours` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
