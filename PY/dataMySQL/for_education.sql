create database Employees;
show databases;
use for_education;
show tables;
select * from collaborators;
select * from persons;

ALTER TABLE collaborators MODIFY COLUMN id int auto_increment;
ALTER TABLE collaborators CHANGE nombre name varchar(255);
alter table collaborators add after_name varchar(255) AFTER nombre;
alter table collaborators modify column social_security varchar(255) after age;

insert into collaborators (name, after_name, position, salary, age, social_security, address_) values ("Ransel", "Melenciano", "Analista de Datos", 5000, 29,"20185542", "calle no te importa");

SHOW CREATE TABLE collaborators;
CREATE TABLE `collaborators` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `after_name` varchar(255) DEFAULT NULL,
  `position` varchar(255) DEFAULT NULL,
  `salary` int DEFAULT NULL,
  `age` int DEFAULT NULL,
  `social_security` varchar(255) DEFAULT NULL,
  `address_` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
insert into collaborators (name, after_name, position, salary, age, social_security, address_) values ("Ransel", "Melenciano", "Analista de Datos", 5000, 29,"20185542", "calle no te importa");
insert into collaborators (name, after_name, position, salary, age, social_security, address_) values ("Ransel", "Melenciano", "Analista de Datos", 5000, 29,"20185542", "calle no te importa");
insert into collaborators (name, after_name, position, salary, age, social_security, address_) values ("Ransel", "Melenciano", "Analista de Datos", 5000, 29,"20185542", "calle no te importa");
insert into collaborators (name, after_name, position, salary, age, social_security, address_) values ("Ransel", "Melenciano", "Analista de Datos", 5000, 29,"20185542", "calle no te importa");
insert into collaborators (name, after_name, position, salary, age, social_security, address_) values ("Ransel", "Melenciano", "Analista de Datos", 5000, 29,"20185542", "calle no te importa");
