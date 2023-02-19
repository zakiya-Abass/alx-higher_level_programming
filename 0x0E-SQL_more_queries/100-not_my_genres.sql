-- List all genres not linked to the show Dexter
SELECT tv_genres.name FROM tv_genres
LEFT JOIN
(SELECT tv_genres.name FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
RIGHT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = "Dexter") dexter ON tv_genres.name = dexter.name
WHERE dexter.name IS NULL
ORDER BY tv_genres.name ASC;
