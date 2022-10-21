SELECT
    Name
FROM
    Employee t1 JOIN
    (SELECT
        ManagerId
    FROM
        Employee
    GROUP BY ManagerId
    HAVING COUNT(ManagerId) >= 5) t2
    ON t1.Id = t2.ManagerId
;