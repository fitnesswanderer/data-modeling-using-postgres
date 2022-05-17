# DROP TABLES
songplay_table_drop = "DROP table if exists songplays"
user_table_drop = "DROP table if exists users"
song_table_drop = "DROP table if exists songs"
artist_table_drop = "DROP table if exists artists"
time_table_drop = "DROP table if exists time"
# CREATE TABLES

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users
    (
    user_id TEXT NOT NULL PRIMARY KEY 
    , first_name VARCHAR 
    , last_name VARCHAR 
    , gender VARCHAR 
    , level VARCHAR 
    )
""")
song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs
    (
    song_id TEXT  NOT NULL PRIMARY KEY 
    , title VARCHAR  NOT NULL
    , artist_id TEXT  NOT NULL 
    , year INT NOT NULL 
    , duration FLOAT NOT NULL 
    )
""")
artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists
    (
    artist_id TEXT  NOT NULL PRIMARY KEY 
    , name VARCHAR  NOT NULL
    , location VARCHAR 
    , latitude FLOAT
    , longitude FLOAT
    )
""")
time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time
    (
    start_time BIGINT NOT NULL PRIMARY KEY 
    , hour INT 
    , day INT  
    , week INT 
    , month INT  
    , year INT 
    , weekday INT 
    )
""")
songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays
    (
    songplay_id SERIAL PRIMARY KEY
    , start_time BIGINT NOT NULL REFERENCES time(start_time)  
    , user_id TEXT NOT NULL REFERENCES users(user_id) 
    , level TEXT
    , song_id TEXT REFERENCES songs(song_id) 
    , artist_id TEXT REFERENCES artists(artist_id)   
    , session_id TEXT
    , location TEXT 
    , user_agent TEXT 
    )
""")
# INSERT RECORDS

user_table_insert = ("""
INSERT INTO users (
    user_id, first_name, last_name, gender, level
)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id)
DO UPDATE 
  SET level=EXCLUDED.level
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
songplay_table_insert = ("""
INSERT INTO songplays (
    start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT DO NOTHING;
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
create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create,songplay_table_create,]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]