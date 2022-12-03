SELECT DISTINCT(page_id) AS recommended_page
FROm Likes
WHERE user_id IN
(
    SELECT DISTINCT(
IF(user1_id = 1, user2_id, user1_id))
    FROM Friendship
    WHERE user1_id = 1 OR user2_id = 1
) AND page_id NOT IN
(
    SELECT page_id AS liked
FROM Likes
WHERE user_id = 1
    
)