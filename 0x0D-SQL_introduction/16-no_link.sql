-- lists all the records of second_table except rows that
-- dont have a name
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC
