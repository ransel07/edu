-- CONSULTAS LAPTOP --


--
select c.after_name, a.marca from collaborators c 
join article a on id = created_by;

select position, after_name from employees_2023 
where salary = (select max(salary) from employees_2023);

select id, position from employees_2023
where salary > (select avg(salary) from employees_2023);

select position, salary from employees_2023
where working_hours < 48;

select position, salary from employees_2023
where working_hours > 48;

select id, position,  working_hours from employees_2023
where age > 30;



-- CONSULTAS DE LA TABLA PRODUCTOS -- 

select name, price from products
where price = (select max(price) from products);

SELECT AVG(price) FROM products;

SELECT name, model, price * stock AS Total FROM products
WHERE name = "Graphic Card";

SELECT name, model, price * stock AS Total FROM products;

SELECT AVG(price * stock) FROM products;

SELECT COUNT(*) FROM products
WHERE company = "Apple";

SELECT id, MODEL FROM productS
WHERE price = (SELECT MAX(price) FROM products);

SELECT id, name, model, (price * stock) FROM products;

SELECT sum(price * stock) AS TOTAL FROM products;

SELECT id, name, model FROM products
WHERE price >= (SELECT AVG(price) FROM products) AND
stock < (SELECT AVG(stock) FROM products);



show tables;