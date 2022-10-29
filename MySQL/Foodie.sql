SELECT ROUND((COUNT(delivery_id) / (SELECT COUNT(delivery_id)
    FROM Delivery)) * 100, 2) AS immediate_percentage
FROM Delivery
WHERE DATEDIFF(order_date,customer_pref_delivery_date) = 0