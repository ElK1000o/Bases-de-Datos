-- Problema 1

SELECT DISTINCT jobTitle, state 
FROM employees, offices 
WHERE state = "CA";

-- Problema 2

SELECT c.customerName AS nombre, SUM(p.amount) as monto 
FROM customers AS c
LEFT OUTER JOIN payments AS p ON c.customerNumber = p.customerNumber
GROUP BY customerName;


-- Problema 3

SELECT checkNumber 
FROM payments 
WHERE paymentDate BETWEEN "2004-01-01" AND "2004-12-31";

-- Problema 4

SELECT COUNT(checkNumber)
FROM payments 
WHERE paymentDate BETWEEN "2003-01-01" AND "2004-12-31";

-- Problema 5

SELECT MAX(amount) AS mayor, MIN(amount) AS menor  
FROM payments;

-- Problema 6

SELECT AVG(amount) 
FROM payments 
WHERE paymentDate BETWEEN "2004-01-01" AND "2004-12-31";

-- Problema 7

SELECT DISTINCT productLine
FROM products;

-- Problema 8

SELECT DISTINCT productLine, SUM(quantityInStock)
FROM products
WHERE productLine LIKE "%Cars%";

-- Problema 9

SELECT productLine, SUM(quantityInStock)
FROM products
WHERE productLine LIKE "%Cars%"
GROUP BY products.productLine;

SELECT products.productLine, SUM(products.quantityInStock)
FROM products
GROUP BY products.productLine
HAVING products.productLine LIKE "%Cars%";

/*
Duda... 
Ambos resultados arrojan lo mismo, 
independiente de usar WHERE o HAVING en GROUP BY,
será por el orden?
*/

-- Problema 10

SELECT p.productCode, quantityOrdered, productLine
FROM products AS p
LEFT OUTER JOIN orderdetails AS o ON p.productCode = o.productCode
GROUP BY productCode;