SELECT price Precio, 
	IF (price > (SELECT AVG(price) FROM sex_toys), "Por arriba", "Por debajo") Estado
FROM sex_toys;

SELECT name Nombre, (price * stock) Total, 
	IF ((SELECT AVG(Total) FROM sex_toys) < (price * stock), "Es mayor", "Es menor") s
FROM sex_toys;









































