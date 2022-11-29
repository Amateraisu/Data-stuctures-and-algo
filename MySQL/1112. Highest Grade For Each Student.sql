SELECT e.student_id, MIN(e.course_id) AS course_id, e.grade
FROM Enrollments e
    JOIN
    (
    SELECT student_id, MAX(grade) AS grade
    FROM Enrollments
    GROUP BY student_id
    
) t
    ON e.student_id = t.student_id AND e.grade = t.grade
GROUP BY e.student_id
ORDER BY student_id ASC, course_id ASC