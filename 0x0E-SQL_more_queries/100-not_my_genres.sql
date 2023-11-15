-- list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
-- You can use a maximum of two SELECT statement

SELECT  name FROM tv_genres 
EXCEPT
SELECT name FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE title = "Dexter"
ORDER BY name;
