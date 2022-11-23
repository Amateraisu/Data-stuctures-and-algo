SELECT w.name AS warehouse_name, SUM(w.units * t.volume) AS volume
FROM Warehouse w
    LEFT JOIN
    (
    SELECT product_id, Width * Length * Height AS volume
    FROM Products 
) t
    ON t.product_id = w.product_id
GROUP BY name