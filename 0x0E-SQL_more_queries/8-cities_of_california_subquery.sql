-- list all cities
SELECT id, name
FROM cities
WHERE state_id = ( -- Query to get the id of Cal
      SELECT id
      FROM states
      WHERE name = "California");
