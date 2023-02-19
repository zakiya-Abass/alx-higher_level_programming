-- List all records of second_table where name is not NULL
-- Display just score and name and in descending order of score
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
