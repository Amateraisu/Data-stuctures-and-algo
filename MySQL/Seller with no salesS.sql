SELECT seller_name
FROM Seller
WHERE  seller_id NOT IN (
    SELECT DISTINCT seller_id
FROM Orders
WHERE SUBSTR(sale_date, 1, 4) = '2020'
)
ORDER BY 1