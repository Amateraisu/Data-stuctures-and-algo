SELECT DISTINCT(l.page_id) AS recommended_page
FROM
    Likes l
WHERE 
l.user_id IN 
(
            SELECT f.user1_id
        FROM Friendship f
        WHERE f.user2_id = 1
    UNION
        SELECT f2.user2_id
        FROM Friendship f2
        WHERE f2.user1_id = 1
    
)
    AND
    l.page_id NOT IN 
(
    SELECT page_id
    FROM Likes
    WHERE user_id = 1 
)