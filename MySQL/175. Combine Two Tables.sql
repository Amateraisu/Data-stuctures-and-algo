SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
    LEFT JOIN Address a
    ON p.personId = a.personId
GROUP BY p.firstName, p.lastName