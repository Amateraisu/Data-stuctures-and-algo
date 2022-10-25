SELECT c.country_name,
    (
    CASE 
        WHEN w.average <= 15 THEN "Cold"
        WHEN w.average >= 25 THEN "Hot"
        ELSE "Warm"
    END

) AS weather_type
FROM
    Countries c
    JOIN
    (
    SELECT country_id, AVG(weather_state) as average
    FROM Weather
    WHERE SUBSTR(day, 6, 2) = "11"
    GROUP BY country_id
) w
    ON w.country_id = c.country_id