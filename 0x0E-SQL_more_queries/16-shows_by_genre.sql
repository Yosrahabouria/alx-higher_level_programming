-- lists all shows, and all genres linked to that show, from a database
SELECT tv_genres.name AS name, tv_shows.title AS title
FROM tv_shows

LEFT OUTER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id

LEFT OUTER JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id

ORDER BY name ASC, BY title ASC;
