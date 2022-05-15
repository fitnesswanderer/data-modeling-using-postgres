# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS user;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist;"
time_table_drop = "DROP TABLE IF EXISTS time;"
# CREATE TABLES
time_table_create = ("CREATE TABLE IF NOT EXISTS time( \
                       start_time time PRIMARY KEY, \
                       hour int, \
                       day int, \
                       week int, \
                       month int, \
                       year int, \
                       weekday varchar);")
cur.execute(time_table_create)
conn.commit()

user_table_create = ("CREATE TABLE IF NOT EXISTS user( \
                           user_id int PRIMARY KEY, \
                           first_name varchar,\
                           last_name varchar, \
                           gender varchar,\
                           level varchar);")
cur.execute(user_table_create)
conn.commit()


artist_table_create = ("CREATE TABLE IF NOT EXISTS artist\
                       (artist_id int, name varchar, location varchar, latitude int, longitude int);")

cur.execute(artist_table_create)
conn.commit()


songplay_table_create = ("CREATE TABLE IF NOT EXISTS songplay( \
                           songplay_id int PRIMARY KEY, \
                           start_time time REFERENCES time,\
                           user_id int REFERENCES user, \
                           level varchar, \
                           song_id varchar,  \
                           artist_id varchar REFERENCES artist, \
                           session_id int, \
                           location text, \
                           user_agent text);")
cur.execute(songplay_table_create)
conn.commit()
                           
                          


song_table_create = ("CREATE TABLE IF NOT EXISTS song( \
                           song_id int PRIMARY KEY, \
                           title varchar,\
                           artist_id int REFERENCES artist, \
                           year int,\
                           duration int);")
cur.execute(song_table_create)
conn.commit()

# INSERT RECORDS
time_table_insert = ("INSERT INTO time(start_time, hour,day,week,month,year,weekday)\ 
                      VALUES(%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING")


songplay_table_insert = ("INSERT INTO songplay(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location,\
                          user_agent) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING")

user_table_insert = ("INSERT INTO user (user_id, first_name, last_name, gender, level)\
                      VALUES(%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING")

song_table_insert = ("INSERT INTO song (song_id, title, artist_id, year, duration)\
                      VALUES(%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING")

artist_table_insert = ("INSERT INTO artist (artist_id, name,location,latitude,longitude) \
                         VALUES(%s,%s,%s,%s,%s) ON CONFLICT DO NOTHING")



# FIND SONGS

song_select = ("SELECT song_id,title, artist_id, year, duration FROM song;")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
