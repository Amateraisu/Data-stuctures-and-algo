SELECT seller_name
FROM Seller
WHERE  seller_id NOT IN (
    SELECT DISTINCT seller_id
FROM Orders
WHERE LEFT(sale_date, 4) = '2020'
)
ORDER BY seller_name ASC