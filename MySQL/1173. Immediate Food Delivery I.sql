
SELECT ROUND(COUNT(delivery_id) * 100 / (SELECT COUNT(delivery_id)
    FROM Delivery), 2) AS immediate_percentage
FROM Delivery
WHERE order_date = customer_pref_delivery_date