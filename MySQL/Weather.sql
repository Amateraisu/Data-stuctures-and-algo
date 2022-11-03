SELECT c.country_name,
    (
    CASE 
        WHEN SUM(w.weather_state) / COUNT(w.day) <= 15 THEN "Cold"
        WHEN SUM(w.weather_state) / COUNT(w.day) >= 25 THEN "Hot"
        ELSE "Warm"
    END
)  AS weather_type

FROM Countries c
    JOIN Weather w
    ON w.country_id = c.country_id
        AND SUBSTR(w.day, 1, 7) = "2019-11"
GROUP BY c.country_name