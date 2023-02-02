# Write your MySQL query statement below
SELECT name 
FROM SalesPerson 
WHERE name NOT IN (SELECT s.name
FROM SalesPerson AS s
INNER JOIN (SELECT o.sales_id
FROM Company AS c
LEFT JOIN Orders AS o
ON c.com_id = o.com_id
WHERE c.name = 'RED') AS t
ON s.sales_id = t.sales_id)
;