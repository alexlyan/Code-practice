-- https://www.codewars.com/kata/5817b124e7f4576fd00020a2/
-- Relational division: Find all movies two actors cast in together

WITH actor_cast AS
(SELECT 
actor_id
 FROM actor
WHERE actor_id = 105 OR actor_id = 122
 
)
SELECT title
FROM (
SELECT f.title, RANK() OVER(PARTITION BY f.title ORDER BY fa.actor_id) AS rank
FROM film f, film_actor fa, actor_cast a
WHERE fa.film_id = f.film_id 
AND fa.actor_id = a.actor_id) as subquery
WHERE rank >= 2;

# Solution 2

SELECT f.title
FROM film f
JOIN film_actor fa on fa.film_id = f.film_id
WHERE fa.actor_id IN (105,122)
GROUP BY f.film_id
HAVING COUNT(*) = 2
ORDER BY f.title ASC
