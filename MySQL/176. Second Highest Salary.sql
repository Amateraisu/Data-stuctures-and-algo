SELECT
IF(COUNT(salary) >= 1, salary, NULL) AS "SecondHighestSalary"
FROM
(
SELECT DISTINCT(salary)
FROM Employee
ORDER BY salary DESC 
LIMIT 1 OFFSET
1
) t1
