--   lists all records with a score >= 10
--  query to list score in second table
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
