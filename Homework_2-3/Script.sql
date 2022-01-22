create table if not exists genre (
	id serial primary key,
	name text not null unique
);

create table if not exists artist (
	id serial primary key,
	name text not null unique,
	genre_id integer references genre(id)
);

create table if not exists album (
	id serial primary key,
	name text not null unique,
	year integer not null check(year > 0),
	artist_id integer references artist(id)
);

create table if not exists track (
	id serial primary key,
	name text not null unique,
	duration integer not null,
	album_id integer references album(id)
);

create table if not exists compilation (
	id serial primary key,
	name text not null unique,
	year integer not null check(year > 0)
);

create table if not exists genreartist (
	id serial primary key,
	genre_id integer references genre(id),
	artist_id integer references artist(id)
);

create table if not exists artistalbum (
	id serial primary key,
	album_id integer references album(id),
	artist_id integer references artist(id)
);

create table if not exists compilationtrack (
	id serial primary key,
	track_id integer references track(id),
	compilation_id integer references compilation(id)
);