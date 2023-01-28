SELECT * FROM persons INNER JOIN orders ON persons.id = orders.order_by;

SELECT orders.name, persons.name 
FROM orders 
JOIN persons ON persons.id = orders.order_by;

SELECT persons.name, orders.name, (orders.price*orders.ud)
FROM orders LEFT JOIN persons
ON persons.id = orders.order_by;

SET @age = 25;

SELECT age FROM persons 
HAVING age > @age;

SELECT persons.name Nombre, persons.age Edad, 
SUM(price) Suma_Precios, SUM(ud) Unidades_Ordenadas, SUM(orders.price * orders.ud) Suma 
FROM orders
LEFT JOIN persons ON persons.id = orders.order_by
GROUP BY orders.order_by;


















