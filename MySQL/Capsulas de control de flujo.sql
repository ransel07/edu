SELECT price Precio, 
	IF (price > (SELECT AVG(price) FROM sex_toys), "Por arriba", "Por debajo") Estado
FROM sex_toys;

SELECT name Nombre, (price * stock) Total, 
	IF ((SELECT AVG(Total) FROM sex_toys) < (price * stock), "Es mayor", "Es menor") s
FROM sex_toys;

SELECT name Nombre,
	IF(age <= 17, "Adolecente",
		IF(age >= 42, "Adulto Mayor", "Adulto")) AS Categoria
FROM clients;

SELECT concepto, Débito,
	IF (Débito BETWEEN 1300 AND 1400, "HERE", "N/A") as dsds
FROM banreservas_historial;

SELECT concepto, Débito 
FROM banreservas_historial
WHERE Débito > 1000;


CREATE TABLE `banreservas_historial` (
  `index` bigint DEFAULT NULL,
  `Producto` bigint DEFAULT NULL,
  `Fecha` text,
  `Concepto` text,
  `Id de transacción` bigint DEFAULT NULL,
  `Débito` text,
  `Crédito` text,
  `Balance` text,
  `Descripción` text,
  `Referencia` bigint DEFAULT NULL,
  KEY `ix_banreservas_historial_index` (`index`)
);




































