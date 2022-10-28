SELECT sale_date, SUM(
IF(fruit = "apples", sold_num, -1 * sold_num)) AS diff 
FROM Sales
GROUP BY sale_date 
ORDER BY sale_date;