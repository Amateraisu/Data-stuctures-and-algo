SELECT c.name AS country
FROM person p
    JOIN Country c
    ON SUBSTR(p.phone_number,1, 3) = c.country_code
    JOIN Calls c1
    ON p.id IN (c1.caller_id, c1.callee_id)
GROUP BY c.name
HAVING AVG(c1.duration)  > (SELECT AVG(duration)
FROM calls)