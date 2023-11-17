--  script that lists all cities contained in the database
--  query to list all cities
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id;
