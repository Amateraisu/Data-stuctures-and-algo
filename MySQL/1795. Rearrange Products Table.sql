    SELECT product_id, store1 AS price, "store1" AS store
    FROM Products
    WHERE store1 IS NOT NULL

UNION

    SELECT product_id, store2 AS price, "store2" AS store
    FROM Products
    WHERE store2 IS NOT NULL

UNION

    SELECT product_id, store3 AS price, "store3" AS store
    FROM Products
    WHERE store3 IS NOT NULL