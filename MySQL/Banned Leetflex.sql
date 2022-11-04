
SELECT DISTINCT a.account_id
FROM LogInfo a
    JOIN LogInfo b 
WHERE a.login BETWEEN (b.login) AND (b.logout)
    AND a.account_id = b.account_id
    and a.ip_address != b.ip_address