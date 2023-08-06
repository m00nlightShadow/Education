# Зміни в базі данних movies:
* додано стовпчик 'year', який відображає рік виходу фільму
* додано стовпчик 'genres', який відображає жанр фільму відповідно

Запит, який знайде всі дані з усіма пов'язаними даними:

select title, directors, actors, genres, year
from movies
inner join directors on (directors.id = director_id)
inner join actors on (actors.id = actor_id);