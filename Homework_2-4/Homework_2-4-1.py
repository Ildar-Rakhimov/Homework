import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://-:-@localhost:5432/-')
connection = engine.connect()

# Создаём таблицы

connection.execute("""
create table if not exists genre (
    id serial primary key,
    name text not null unique
);
""")

connection.execute("""
create table if not exists artist (
    id serial primary key,
    name text not null unique
);
""")

connection.execute("""
create table if not exists album (
    id serial primary key,
    name text not null unique,
    year integer not null check(year > 0)
);
""")

connection.execute("""
create table if not exists track (
    id serial primary key,
    name text not null unique,
    duration integer not null,
    album_id integer references album(id)
);
""")

connection.execute("""
create table if not exists compilation (
    id serial primary key,
    name text not null unique,
    year integer not null check(year > 0)
);
""")

connection.execute("""
create table if not exists genre_artist (
    id serial primary key,
    genre_id integer references genre(id),
    artist_id integer references artist(id)
);
""")


connection.execute("""
create table if not exists artist_album (
    id serial primary key,
    album_id integer references album(id),
    artist_id integer references artist(id)
);
""")
