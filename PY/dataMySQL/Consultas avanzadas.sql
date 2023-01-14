show tables;
SELECT SUM(salary) FROM employees_2023;
SELECT AVG(salary) FROM employees_2023;
SELECT MIN(salary) FROM employees_2023;
SELECT MAX(salary), name FROM employees_2023;

SELECT emp1.name, emp2.max_salary FROM employees_2023 emp1 
JOIN (
	SELECT MAX(salary) AS max_salary FROM employees_2023
) emp2 ON emp1.salary = emp2.max_salary;

SELECT e1.after_name, e2.min_ from employees_2023 e1
join (
	select min(salary) as min_ from employees_2023
) e2 on e1.salary = e2.min_;

select e.name, a.name from employees_2023 e 
inner join article a on created_by = id;

select e.position, a.marca from employees_2023 e 
right join article a on created_by = id;

select after_name from employees_2023 order by name desc;



