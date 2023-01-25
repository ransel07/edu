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


















