SELECT order_id
FROM OrdersDetails
GROUP BY order_id
HAVING MAX(quantity) > 
(SELECT MAX(qty)
FROM
    (
    SELECT order_id, AVG(quantity) as qty
    FROM OrdersDetails
    GROUP BY order_id
    
    
) t)