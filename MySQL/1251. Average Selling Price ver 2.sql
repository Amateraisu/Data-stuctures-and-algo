SELECT u.product_id, ROUND(SUM(u.units * p.price) / SUM(u.units) , 2) AS average_price
FROM UnitsSold u
    LEFT JOIN Prices p
    ON p.product_id = u.product_id
        AND
        u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY product_id