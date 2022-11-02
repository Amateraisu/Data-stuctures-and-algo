SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM employee e
    LEFT JOIN department d
    ON e.departmentId = d.id
GROUP BY e.name
HAVING (department, salary) IN 
(
    SELECT d.name, MAX(e.salary)
FROM department d
    JOIN employee e
    ON e.departmentId = d.id
GROUP BY d.name
)