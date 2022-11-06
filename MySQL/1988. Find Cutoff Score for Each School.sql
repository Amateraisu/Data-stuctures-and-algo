SELECT s.school_id, IFNULL(MIN(e.score), -1) AS score
FROM Schools s
    LEFT JOIN
    Exam e
    ON e.student_count <= s.capacity
GROUP BY school_id