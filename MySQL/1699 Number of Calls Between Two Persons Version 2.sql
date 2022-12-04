SELECT c1 AS person1, c2 AS person2, COUNT(c1) AS call_count, SUM(c3) AS total_duration
FROM
    (
    SELECT (IF(from_id < to_id, from_id, to_id)) AS c1, (IF(from_id < to_id, to_id, from_id
)) AS c2, duration AS c3
    FROM Calls 
) calls
GROUP BY c1, c2