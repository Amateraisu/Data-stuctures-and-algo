SELECT p.firstName, p.lastName, A.city, A.state
FROM Person p
    LEFT JOIN Address A
    ON p.personId = A.personId;