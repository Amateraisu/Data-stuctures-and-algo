SELECT stu.student_id AS student_id, stu.student_name AS student_name, sub.subject_name AS subject_name,
    COUNT(e.student_id) AS attended_exams
FROM Students stu
    INNER JOIN Subjects sub
    LEFT JOIN Examinations e
    ON e.student_id = stu.student_id AND e.subject_name = sub.subject_name 
GROUP BY stu.student_name, sub.subject_name
ORDER BY student_id, subject_name