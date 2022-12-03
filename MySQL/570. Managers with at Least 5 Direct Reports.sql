SELECT e1.name
FROM Employee e1
    LEFT JOIN Employee e2
    ON e1.id = e2.managerId
GROUP BY name
HAVING COUNT(e2.managerId) >= 5