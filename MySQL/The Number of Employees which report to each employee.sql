SELECT e1.employee_id, e1.name, COUNT(e2.reports_to) AS reports_count, ROUND(SUM(e2.age)/ COUNT(e2.reports_to), 0) AS average_age
FROM Employees e1
    JOIN Employees e2
    ON e2.reports_to = e1.employee_id
GROUP BY e1.employee_id
ORDER BY e1.employee_id