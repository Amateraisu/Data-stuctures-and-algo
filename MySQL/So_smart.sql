SELECT t.student_id, MIN(t2.course_id) AS course_id, t.grade
FROM
    (
    SELECT student_id, MAX(grade) AS grade
    FROM Enrollments
    GROUP BY student_id
) t
    LEFT JOIN Enrollments t2
    ON t2.student_id = t.student_id AND t2.grade = t.grade
GROUP BY t.student_id
ORDER BY t.student_id