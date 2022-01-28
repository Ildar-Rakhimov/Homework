import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://py47:123456@localhost:5432/py47_db')
connection = engine.connect()

# Название и год выхода альбомов, вышедших в 2018 году

pprint(connection.execute("""
SELECT name, year FROM album
WHERE year = 2018;
""").fetchall())

# название и продолжительность самого длительного трека

pprint(connection.execute("""
SELECT name, duration FROM track
ORDER BY duration DESC
LIMIT 1;
""").fetchall())

# название треков, продолжительность которых не менее 3,5 минуты

pprint(connection.execute("""
SELECT name FROM track
WHERE duration >= 210;
""").fetchall())

# названия сборников, вышедших в период с 2018 по 2020 год включительно

pprint(connection.execute("""
SELECT name FROM compilation
WHERE year BETWEEN 2018 AND 2020;
""").fetchall())

# исполнители, чье имя состоит из 1 слова

pprint(connection.execute("""
SELECT name FROM artist
WHERE name NOT LIKE '%% %%';
""").fetchall())

# название треков, которые содержат слово "мой"/"my"

pprint(connection.execute("""
SELECT name FROM track
WHERE name iLIKE '%%my%%' OR name iLIKE '%%мой%%';
""").fetchall())
