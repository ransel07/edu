SHOW CREATE TABLE employees_2023;

CREATE TABLE employees_2023 (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(255) DEFAULT NULL,
  after_name varchar(255) DEFAULT NULL,
  position varchar(255) DEFAULT NULL,
  salary int DEFAULT NULL,
  age int DEFAULT NULL,
  working_hours int DEFAULT NULL,
  PRIMARY KEY (id)
);


insert into employees_2023(name, after_name, position, salary, age, working_hours)
values
	("Ransel", "Melenciano", "Analista de Datos", 5000, 27, 48),
    ("Juan", "Molina", "Programador", 1500, 26, 48),
    ("Ana", "Fernandez", "Analista de Datos", 2000, 27, 40),
    ("Pedro", "Morrinson", "Jefe de proyecto", 2500, 30, 42),
    ("Sofía", "Martinez", "Gerente de TI", 3000, 28, 50),
    ("Mauricio", "Lopez", "Desarrollador", 2000, 25, 40),
    ("Carlos", "Garcia", "Analista Financiero", 3500, 32, 45),
    ("Marcela", "Perez", "Recursos Humanos", 2500, 29, 40),
    ("Jorge", "Sanchez", "Contador", 3000, 35, 40),
    ("Maria", "Rodriguez", "Marketing", 2000, 27, 40),
    ("Diego", "Martinez", "Ventas", 2500, 30, 40),
    ("Andrea", "Garcia", "Compras", 2000, 25, 40),
	("Juan", "Perez", "Gerente de Operaciones", 3500, 32, 45),
	("Isabella", "Sanchez", "Jefe de Recursos Humanos", 3000, 35, 40),
	("Sebastian", "Rodriguez", "Jefe de Finanzas", 2500, 30, 40),
	("Valeria", "Martinez", "Jefe de Marketing", 2000, 27, 40),
	("Mateo", "Garcia", "Jefe de Ventas", 2500, 30, 40),
	("Catalina", "Perez", "Jefe de Compras", 2000, 25, 40),
	("Dario", "Sanchez", "Jefe de Producción", 3500, 32, 45),
	("Antonia", "Rodriguez", "Jefe de Logística", 3000, 35, 40),
	("Emiliano", "Martinez", "Jefe de Tecnología", 2500, 30, 40);

