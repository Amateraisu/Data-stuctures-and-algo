SELECT employee_id, team_size
FROM Employee e
    LEFT JOIN (
      SELECT team_id, COUNT(DISTINCT employee_id) team_size
    FROM Employee
    GROUP BY team_id
) AS teams
    ON e.team_id = teams.team_id