SELECT * FROM persons INNER JOIN orders ON persons.id = orders.order_by;

SELECT orders.name, persons.name 
FROM orders 
JOIN persons ON persons.id = orders.order_by;

SELECT orders.name
