SELECT prices.product_id, ROUND(SUM(prices.price * u.units) / SUM(u.units), 2) AS average_price
FROM Prices
    LEFT JOIN UnitsSold u
    ON u.product_id = prices.product_id AND (u.purchase_date BETWEEN prices.start_date AND prices.end_date)
GROUP BY product_id;