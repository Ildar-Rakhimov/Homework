import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://-:-@localhost:5432/-')
connection = engine.connect()

# изменим год альбома "CArBru + Pertur" на 2019  для наглядности при выполнении запросов

# connection.execute("""
# UPDATE album
# SET year = 2019
# WHERE id = 11;
# """)

# изменим длительность песни "I'm Not Okay (I Promise)" на 195 для наглядности при выполнении запросов
#
# connection.execute("""
# UPDATE track
# SET duration  = 195
# WHERE id = 29;
# """)

# добавим треки
#
# connection.execute("""
# INSERT INTO track(id, name, duration, album_id)
#     VALUES(34, 'Sleep', 283, 1),
#     (35, 'American Idiot', 176, 2),
#     (36, 'Whatsername', 257, 2),
#     (37, 'Alone Again', 250, 3),
#     (38, 'Last Kiss', 284, 8);
# """)

# 1. количество исполнителей в каждом жанре

pprint(connection.execute("""
SELECT genre.name, COUNT(artist_id) FROM genre_artist
LEFT JOIN genre ON genre_artist.genre_id = genre.id
GROUP BY genre.name;
""").fetchall())

# 2. количество треков, вошедших в альбомы 2019-2020 годов

pprint(connection.execute("""
SELECT COUNT(track.name) FROM track
LEFT JOIN album ON track.album_id = album.id
WHERE year IN (2019, 2020);
""").fetchall())

# 3. средняя продолжительность треков по каждому альбому

pprint(connection.execute("""
SELECT album.name, ROUND(AVG(duration), 2) FROM track
LEFT JOIN album ON track.album_id = album.id
GROUP BY album.name;
""").fetchall())

# 4. все исполнители, которые не выпустили альбомы в 2020 году

pprint(connection.execute("""
SELECT artist.name FROM artist
JOIN artist_album ON artist.id = artist_album.artist_id
JOIN album ON artist_album.album_id = album.id
WHERE album.year != 2020
GROUP BY artist.name;
""").fetchall())

# 5. названия сборников, в которых присутствует конкретный исполнитель (выберите сами)

pprint(connection.execute("""
SELECT compilation.name FROM compilation
JOIN compilation_track ON compilation.id = compilation_track.compilation_id
JOIN track ON compilation_track.track_id = track.id
JOIN album ON track.album_id = album.id
JOIN artist_album ON album.id = artist_album.album_id
JOIN artist ON artist_album.artist_id = artist.id
WHERE artist.name = 'The Weeknd'
GROUP BY compilation.name;
""").fetchall())

# 6. название альбомов, в которых присутствуют исполнители более 1 жанра

pprint(connection.execute("""
SELECT album.name FROM album
JOIN artist_album ON album.id = artist_album.album_id
JOIN artist ON artist_album.artist_id = artist.id
JOIN genre_artist ON artist.id = genre_artist.artist_id
JOIN genre ON genre_artist.genre_id = genre.id
GROUP BY album.name
HAVING COUNT(DISTINCT genre.id) > 1;
""").fetchall())

# 7. наименование треков, которые не входят в сборники

pprint(connection.execute("""
SELECT track.name FROM track
FULL OUTER JOIN compilation_track ON track.id = compilation_track.track_id
FULL OUTER JOIN compilation ON compilation_track.compilation_id = compilation.id
WHERE compilation.name IS NULL
GROUP BY track.name;
""").fetchall())

# 8. исполнителя(-ей), написавшего самый короткий по продолжительности трек

pprint(connection.execute("""
SELECT artist.name, track.duration FROM artist
JOIN artist_album ON artist.id = artist_album.artist_id
JOIN album ON artist_album.album_id = album.id
JOIN track ON album.id = track.album_id
WHERE track.duration = (
SELECT MIN(duration) FROM track);
""").fetchall())

# 9. название альбомов, содержащих наименьшее количество треков

pprint(connection.execute("""
SELECT album.name FROM album
JOIN track ON album.id = track.album_id
GROUP BY album.name
HAVING COUNT(track.id) = (
SELECT COUNT(track.id) FROM album
JOIN track ON album.id = track.album_id
GROUP BY album.name
ORDER BY COUNT(track.id)
LIMIT 1);
""").fetchall())