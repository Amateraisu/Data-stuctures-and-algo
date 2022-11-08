# Write your
MySQL query statement below


#
SELECT title, average_rating 
#
FROM
    # (
#
SELECT m.title, SUM(mov.rating) / COUNT(mov.rating) AS average_rating
#     FROM Movies m 
#     JOIN MovieRating mov 
#     ON m.movie_id = mov.movie_id 
#     WHERE mov.created_at LIKE "2020-02%"
#     GROUP BY m.title
    
    
# ) t
# ORDER

SELECT name AS results
FROM (
    SELECT u.name, COUNT(m.user_id) AS num_rated
    FROM Users u
        JOIN MovieRating m
        ON u.user_id = m.user_id
    GROUP BY u.name
    ORDER BY num_rated DESC , name ASC
    LIMIT 1 
    
    
) t

UNION 

SELECT title 
FROM (
    
    SELECT m.title, SUM(mov.rating) / COUNT(mov.rating) AS average_rating
    FROM Movies m
        JOIN MovieRating mov
        ON m.movie_id = mov.movie_id
    WHERE mov.created_at LIKE "2020-02%"
    GROUP BY m.title
    ORDER BY average_rating DESC, m.title ASC
    LIMIT 1 
    
) t1