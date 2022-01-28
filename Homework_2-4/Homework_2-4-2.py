import sqlalchemy
from pprint import pprint

engine = sqlalchemy.create_engine('postgresql://-:-@localhost:5432/-')
connection = engine.connect()

# Заполняем таблицу "genre"

connection.execute("""
INSERT INTO genre
    VALUES(1, 'Rock');
""")

connection.execute("""
INSERT INTO genre
    VALUES(2, 'Pop');
""")

connection.execute("""
INSERT INTO genre
    VALUES(3, 'Classical');
""")

connection.execute("""
INSERT INTO genre
    VALUES(4, 'Electronic');
""")

connection.execute("""
INSERT INTO genre
    VALUES(5, 'Rap');
""")

# Заполняем таблицу "artist"

connection.execute("""
INSERT INTO artist
    VALUES(1, 'The Weeknd');
""")

connection.execute("""
INSERT INTO artist
    VALUES(2, 'My Chemical Romance');
""")

connection.execute("""
INSERT INTO artist
    VALUES(3, 'Green Day');
""")

connection.execute("""
INSERT INTO artist
    VALUES(4, 'Eminem');
""")

connection.execute("""
INSERT INTO artist
    VALUES(5, 'Antonio Vivaldi');
""")

connection.execute("""
INSERT INTO artist
    VALUES(6, 'Frederic Chopin');
""")

connection.execute("""
INSERT INTO artist
    VALUES(7, 'Perturbator');
""")

connection.execute("""
INSERT INTO artist
    VALUES(8, 'Carpenter Brut');
""")

# Заполняем таблицу "album"

connection.execute("""
INSERT INTO album
    VALUES(1, 'The Black Parade', 2006);
""")

connection.execute("""
INSERT INTO album
    VALUES(2, 'American Idiot', 2004);
""")

connection.execute("""
INSERT INTO album
    VALUES(3, 'After Hours', 2020);
""")

connection.execute("""
INSERT INTO album
    VALUES(4, 'Trilogy', 2015);
""")

connection.execute("""
INSERT INTO album
    VALUES(5, 'The Eminem Show', 2002);
""")

connection.execute("""
INSERT INTO album
    VALUES(6, 'Vivaldi: Classical Masterpieces', 2018);
""")

connection.execute("""
INSERT INTO album
    VALUES(7, 'Some Chopin', 2018);
""")

connection.execute("""
INSERT INTO album
    VALUES(8, 'Dangerous Days', 2014);
""")

connection.execute("""
INSERT INTO album
    VALUES(9, '21st Century Breakdown', 2009);
""")

connection.execute("""
INSERT INTO album
    VALUES(10, 'Three Cheers For Sweet Revenge', 2004);
""")

connection.execute("""
INSERT INTO album
    VALUES(11, 'CarBru + Pertur', 2022);
""")

# Заполняем таблицу "track"

connection.execute("""
INSERT INTO track
    VALUES(1, 'Welcome To The Black Parade', 311, 1);
""")

connection.execute("""
INSERT INTO track
    VALUES(2, 'I Don''t Love You', 238, 1);
""")

connection.execute("""
INSERT INTO track
    VALUES(3, 'Mama', 279, 1);
""")

connection.execute("""
INSERT INTO track
    VALUES(4, 'Jesus Of Suburbia', 548, 2);
""")

connection.execute("""
INSERT INTO track
    VALUES(5, 'Boulevard Of Broken Dreams', 260, 2);
""")

connection.execute("""
INSERT INTO track
    VALUES(6, 'Homecoming', 558, 2);
""")

connection.execute("""
INSERT INTO track
    VALUES(7, 'Blinding Lights', 200, 3);
""")

connection.execute("""
INSERT INTO track
    VALUES(8, 'In Your Eyes', 237, 3);
""")

connection.execute("""
INSERT INTO track
    VALUES(9, 'Save Your Tears', 215, 3);
""")

connection.execute("""
INSERT INTO track
    VALUES(10, 'Le perv', 256, 4);
""")

connection.execute("""
INSERT INTO track
    VALUES(11, 'Roller Mobster', 214, 4);
""")

connection.execute("""
INSERT INTO track
    VALUES(12, 'Paradise Warfare', 256, 4);
""")

connection.execute("""
INSERT INTO track
    VALUES(13, 'Sing For The Moment', 339, 5);
""")

connection.execute("""
INSERT INTO track
    VALUES(14, 'When The Music Stops', 269, 5);
""")

connection.execute("""
INSERT INTO track
    VALUES(15, '''Till I Collapse', 297, 5);
""")

connection.execute("""
INSERT INTO track
    VALUES(16, 'Spring', 211, 6);
""")

connection.execute("""
INSERT INTO track
    VALUES(17, 'Summer', 318, 6);
""")

connection.execute("""
INSERT INTO track
    VALUES(18, 'Winter', 206, 6);
""")

connection.execute("""
INSERT INTO track
    VALUES(19, 'Nocturne in E-Flat Major, Op. 9, No. 2', 284, 7);
""")

connection.execute("""
INSERT INTO track
    VALUES(20, 'Nocturne in C-Sharp Minor, B. 49', 232, 7);
""")

connection.execute("""
INSERT INTO track
    VALUES(21, 'Nocturne in E Minor, Op. 72, No. 1', 394, 7);
""")

connection.execute("""
INSERT INTO track
    VALUES(22, 'Perturbator''s Theme', 336, 8);
""")

connection.execute("""
INSERT INTO track
    VALUES(23, 'Future Club', 289, 8);
""")

connection.execute("""
INSERT INTO track
    VALUES(24, 'Dangerous Days', 727, 8);
""")

connection.execute("""
INSERT INTO track
    VALUES(25, '21st Century Breakdown', 309, 9);
""")

connection.execute("""
INSERT INTO track
    VALUES(26, 'Horseshoes And Handgrenades', 194, 9);
""")

connection.execute("""
INSERT INTO track
    VALUES(27, 'See The Light', 275, 9);
""")

connection.execute("""
INSERT INTO track
    VALUES(28, 'Helena', 204, 10);
""")

connection.execute("""
INSERT INTO track
    VALUES(29, 'I''m Not Okay (I Promise)', 186, 10);
""")

connection.execute("""
INSERT INTO track
    VALUES(30, 'The Ghost Of You', 194, 10);
""")

connection.execute("""
INSERT INTO track
    VALUES(31, 'My Sacrifice', 326, 11);
""")

connection.execute("""
INSERT INTO track
    VALUES(32, 'You And Me', 414, 11);
""")

connection.execute("""
INSERT INTO track
    VALUES(33, 'Red Sky', 399, 11);
""")

# Заполняем таблицу "compilation"

connection.execute("""
INSERT INTO compilation
    VALUES(1, 'Hotline Miami OST', 2015);
""")

connection.execute("""
INSERT INTO compilation
    VALUES(2, 'Classical Music', 2022);
""")

connection.execute("""
INSERT INTO compilation
    VALUES(3, '2000''s Rock Songs', 2010);
""")

connection.execute("""
INSERT INTO compilation
    VALUES(4, 'My Chemical Romance: Greatest Hits', 2015);
""")

connection.execute("""
INSERT INTO compilation
    VALUES(5, 'Rock and Rap', 2015);
""")

connection.execute("""
INSERT INTO compilation
    VALUES(6, 'Pop and Rock', 2020);
""")

connection.execute("""
INSERT INTO compilation
    VALUES(7, 'Pop And Rap', 2020);
""")

connection.execute("""
INSERT INTO compilation
    VALUES(8, 'Green Day: Greatest Hits', 2022);
""")

# Заполняем таблицу "genre_artist"

connection.execute("""
INSERT INTO genre_artist
    VALUES(1, 1, 2);
""")

connection.execute("""
INSERT INTO genre_artist
    VALUES(2, 1, 3);
""")

connection.execute("""
INSERT INTO genre_artist
    VALUES(3, 2, 1);
""")

connection.execute("""
INSERT INTO genre_artist
    VALUES(4, 2, 3);
""")

connection.execute("""
INSERT INTO genre_artist
    VALUES(5, 3, 5);
""")

connection.execute("""
INSERT INTO genre_artist
    VALUES(6, 3, 6);
""")

connection.execute("""
INSERT INTO genre_artist
    VALUES(7, 4, 7);
""")

connection.execute("""
INSERT INTO genre_artist
    VALUES(8, 4, 8);
""")

connection.execute("""
INSERT INTO genre_artist
    VALUES(9, 5, 4);
""")

connection.execute("""
INSERT INTO genre_artist
    VALUES(10, 4, 1);
""")

connection.execute("""
INSERT INTO genre_artist
    VALUES(11, 2, 4);
""")

# Заполняем таблицу "artist_album"

connection.execute("""
INSERT INTO artist_album
    VALUES(1, 1, 2);
""")

connection.execute("""
INSERT INTO artist_album
    VALUES(2, 2, 3);
""")

connection.execute("""
INSERT INTO artist_album
    VALUES(3, 3, 1);
""")

connection.execute("""
INSERT INTO artist_album
    VALUES(4, 4, 8);
""")

connection.execute("""
INSERT INTO artist_album
    VALUES(5, 5, 4);
""")

connection.execute("""
INSERT INTO artist_album
    VALUES(6, 6, 5);
""")

connection.execute("""
INSERT INTO artist_album
    VALUES(7, 7, 6);
""")

connection.execute("""
INSERT INTO artist_album
    VALUES(8, 8, 7);
""")

connection.execute("""
INSERT INTO artist_album
    VALUES(9, 9, 3);
""")

connection.execute("""
INSERT INTO artist_album
    VALUES(10, 10, 2);
""")

connection.execute("""
INSERT INTO artist_album
    VALUES(11, 11, 8);
""")

connection.execute("""
INSERT INTO artist_album
    VALUES(12, 11, 7);
""")

# Заполняем таблицу "compilation_track"

connection.execute("""
INSERT INTO compilation_track
    VALUES(1, 10, 1);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(2, 11, 1);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(3, 23, 1);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(4, 24, 1);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(5, 17, 2);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(6, 18, 2);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(7, 19, 2);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(8, 21, 2);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(9, 1, 3);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(10, 2, 3);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(11, 4, 3);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(12, 5, 3);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(13, 1, 4);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(14, 3, 4);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(15, 28, 4);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(16, 29, 4);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(17, 13, 5);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(18, 15, 5);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(19, 26, 5);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(20, 30, 5);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(21, 7, 6);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(22, 9, 6);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(23, 25, 6);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(24, 29, 6);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(25, 5, 7);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(26, 8, 7);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(27, 14, 7);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(28, 15, 7);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(29, 4, 8);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(30, 6, 8);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(31, 25, 8);
""")

connection.execute("""
INSERT INTO compilation_track
    VALUES(32, 27, 8);
""")