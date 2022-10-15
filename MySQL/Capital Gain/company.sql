SELECT SalesPerson.name
FROM SalesPerson
WHERE SalesPerson.sales_id NOT IN (
    SELECT Orders.sales_id
FROM Orders
    LEFT JOIN
    Company c ON Orders.com_id = c.com_id
WHERE c.name = "RED"

)