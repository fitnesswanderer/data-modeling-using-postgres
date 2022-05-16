# DROP TABLES
songplay_table_drop = "DROP table if exists songplays"
user_table_drop = "DROP table if exists users"
song_table_drop = "DROP table if exists songs"
artist_table_drop = "DROP table if exists artists"
time_table_drop = "DROP table if exists time"
# CREATE TABLES
songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays
    (
    songplay_id serial NOT NULL PRIMARY KEY
    , start_time bigint NOT NULL
    , user_id int NOT NULL
    , level varchar
    , song_id varchar 
    , artist_id varchar 
    , session_id int NOT NULL
    , location varchar
    , user_agent varchar
    )
""")
user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users
    (
    user_id int NOT NULL PRIMARY KEY
    , first_name varchar NOT NULL
    , last_name varchar
    , gender varchar
    , level varchar
    )
""")
song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs
    (
    song_id varchar NOT NULL PRIMARY KEY
    , title varchar NOT NULL
    , artist_id varchar NOT NULL
    , year int NOT NULL
    , duration float NOT NULL
    )
""")
artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists
    (
    artist_id varchar NOT NULL PRIMARY KEY
    , name varchar NOT NULL
    , location varchar
    , latitude float
    , longitude float
    )
""")
time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time
    (
    start_time bigint NOT NULL PRIMARY KEY
    , hour int NOT NULL
    , day int NOT NULL
    , week int NOT NULL
    , month int NOT NULL
    , year int NOT NULL
    , weekday varchar NOT NULL
    )
""")
# INSERT RECORDS
songplay_table_insert = ("""
INSERT INTO songplays (
    start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING;
""")
user_table_insert = ("""
INSERT INTO users (
    user_id, first_name, last_name, gender, level
)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
;
""")
song_table_insert = ("""
INSERT INTO songs (
    song_id, title, artist_id, year, duration
)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING
;
""")
artist_table_insert = ("""
INSERT INTO artists (
    artist_id, name, location, latitude, longitude
)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING;
""")
time_table_insert = ("""
INSERT INTO time (
    start_time, hour, day, week, month, year, weekday
)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING;
""")
# FIND SONGS
song_select = ("""
SELECT 
    a.song_id
    ,b.artist_id
FROM
    songs a
    JOIN artists b ON a.artist_id=b.artist_id
    
WHERE a.title = %s AND b.name = %s AND a.duration = %s
;
""")
# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]