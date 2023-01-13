create database Employees;
show databases; --
use for_education;
show tables;
select * from employees_2023;
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
ALTER TABLE collaborators drop column address;






insert into collaborators (name, after_name, position_, salary, age, address_,working_hours) VALUES ("Ransel", "Melenciano", "Analista de Datos", 5000, 27,"calle no te importa", 48);


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



