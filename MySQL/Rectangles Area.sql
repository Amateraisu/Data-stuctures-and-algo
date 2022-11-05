SELECT p1.id AS p1 , p2.id AS p2, ABS(p1.x_value - p2.x_value) * ABS(p1.y_value - p2.y_value) AS area
FROM Points p1
    JOIN Points p2 
WHERE p1.id < p2.id
GROUP BY p1.id, p2.id
HAVING area > 0
ORDER BY area DESC, p1 ASC , p2 ASC