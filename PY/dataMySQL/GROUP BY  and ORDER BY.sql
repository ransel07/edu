SELECT age FROM persons ORDER BY age;

SELECT age FROM persons GROUP BY age;

SELECT ud, SUM(ud), count(*) FROM orders GROUP BY ud;

SELECT salary Salario, SUM(salary) Suma, COUNT(*) Cant 
FROM employees_2023 GROUP BY salary
ORDER BY Cant;

SELECT name Nombre, after_name Apellido, age edad, (salary/working_hours) SalarioPorHora 
FROM employees_2023
ORDER BY SalarioPorHora;

SELECT company Compañias, SUM(price), COUNT(*) Cant 
FROM products
GROUP BY company
HAVING Cant > 1;

SELECT ud, COUNT(*) FROM orders
WHERE ud > 100
GROUP BY ud
ORDER BY ud;

SELECT position Puesto, COUNT(*) Cant FROM employees_2023
GROUP BY position 
HAVING Cant > 1
ORDER BY Cant DESC;

SELECT after_name Apellido, SUM(salary), COUNT(*) Cant FROM employees_2023
GROUP BY after_name
HAVING Cant > 1
ORDER BY Cant DESC;

SELECT position Puesto, AVG(salary) SalarioProm, COUNT(*) Cant
FROM employees_2023
GROUP BY Puesto
HAVING Cant > 1 AND SalarioProm > 3200;

SELECT order_by Empleado, SUM(price * ud) Suma FROM orders
GROUP BY order_by
HAVING Suma > (SELECT AVG(price) FROM orders);

































