SELECT e1.employee_id, e2.team_size
FROM Employee e1
    JOIN
    (
    SELECT team_id, COUNT(employee_id) AS team_size
    FROM Employee
    GROUP BY team_id 
    
) e2
    ON e1.team_id = e2.team_id 