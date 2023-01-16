SHOW CREATE TABLE employees_2023;

CREATE TABLE employees_2023 (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(255) DEFAULT NULL,
  after_name varchar(255) DEFAULT NULL,
  position varchar(255) DEFAULT NULL,
  salary int DEFAULT NULL,
  age int DEFAULT NULL,
  working_hours int DEFAULT NULL,
  PRIMARY KEY (id),
  foreign key()
);

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

CREATE TABLE Products (
  id int NOT NULL AUTO_INCREMENT,
  name varchar(255) DEFAULT NULL,
  model varchar(255) DEFAULT NULL,
  company varchar(255) DEFAULT NULL,
  price int DEFAULT NULL,
  stock int DEFAULT NULL,
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

insert into supervisors(name, after_name, position, salary, age, working_hours)
values
    ("Juan Carlos", "Gonzalez", "Director General", 6000, 40, 50),
    ("Sandra", "Lopez", "Gerente General", 5000, 38, 50),
    ("Pablo", "Garcia", "Director de Finanzas", 4500, 42, 45),
    ("Camila", "Perez", "Gerente de Recursos Humanos", 4000, 35, 40),
    ("Felipe", "Sanchez", "Director de Operaciones", 4500, 40, 45),
    ("Valentina", "Rodriguez", "Gerente de Marketing", 3500, 30, 35),
    ("Andres", "Martinez", "Director de Producción", 4500, 40, 45),
    ("Luciana", "Garcia", "Gerente de Logística", 4000, 35, 40),
    ("Santiago", "Perez", "Director de Tecnología", 4500, 40, 45),
    ("Natalia", "Sanchez", "Gerente de Ventas", 3500, 30, 35);

delete from employees_2023 where id > 21;

insert into Products(name, model, company, price, stock)
values
    ("Graphic Card", "3090TI", "Nvidia", 2500, 275),
    ("Processor", "Ryzen 9", "AMD", 500, 50),
    ("RAM", "Corsair DDR4", "Corsair", 100, 1000),
    ("Motherboard", "Z590", "Asus", 250, 200),
    ("Storage", "1TB SSD", "Samsung", 150, 500),
    ("Cooler", "Hyper 212", "Cooler Master", 50, 150),
    ("Power Supply", "850W", "Corsair", 100, 200),
    ("Monitor", "27 inch 4K", "Dell", 400, 150),
    ("Keyboard", "Corsair K95", "Corsair", 150, 100),
    ("Mouse", "Logitech G Pro", "Logitech", 75, 200),
    ("Headphones", "Sennheiser HD 660 S", "Sennheiser", 250, 100),
    ("Speakers", "Creative T100", "Creative", 50, 250),
    ("Mousepad", "Steelseries Qck", "Steelseries", 15, 500),
    ("Webcam", "Logitech C922", "Logitech", 75, 200),
    ("Laptop", "XPS 15", "Dell", 1500, 100),
    ("Tablet", "iPad Pro", "Apple", 700, 200),
    ("Smartphone", "iPhone 12", "Apple", 800, 200),
    ("Smartwatch", "Apple Watch Series 6", "Apple", 400, 100),
    ("Fitness Tracker", "Fitbit Charge 4", "Fitbit", 150, 200);