--  script that lists the number of records with the same score in the table
-- script to list same score numbers
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
