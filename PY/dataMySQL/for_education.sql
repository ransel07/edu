create database Employees;
show databases; --
use for_education;
show tables;
select * from collaborators;
select * from persons;

-- Modificar 
ALTER TABLE collaborators MODIFY COLUMN id int auto_increment;
ALTER TABLE collaborators MODIFY COLUMN working_hours int;

ALTER TABLE collaborators CHANGE nombre name varchar(255);
alter table collaborators add working_hours varchar(255) AFTER age;
alter table collaborators modify column social_security varchar(255) after age;
ALTER TABLE collaborators drop column social_security;


insert into collaborators (name, after_name, position, salary, age, social_security, address_) values ("Ransel", "Melenciano", "Analista de Datos", 5000, 29,"20185542", "calle no te importa");

insert into collaborators (name, after_name, position, salary, age, social_security, address_) values ("Ransel", "Melenciano", "Analista de Datos", 5000, 27,"20185542", "calle no te importa");
insert into collaborators (name, after_name, position, salary, age, social_security, address_) values ("Juan", "Molina", "Programador", 1500, 26,"20175632", "calle villa juana");
insert into collaborators (name, after_name, position, salary, age, social_security, address_) values ("Ana", "Fernandez", "Analista de Datos", 2000, 27,"20181302", "Charles de Gaulle");
insert into collaborators (name, after_name, position, salary, age, social_security, address_) values ("Pedro", "Morrinson", "Jefe de proyecto", 2500, 30,"20181299", "Cancino");
insert into collaborators (name, after_name, position, salary, age, social_security, address_) values ("Sofía", "Martinez", "Gerente de TI", 3000, 28,"20185542", "Residencial las Acacias");
insert into collaborators (id, working_hours) values (1, 47);

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
