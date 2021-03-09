import lyricsgenius
import re
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="helloworld",
    database="seng474"
)
mycursor = mydb.cursor()

genius = lyricsgenius.Genius("vC8OIun7ZiKHPfUUr_3dpEuQ0KqABzeogLshI9NXF8A5iiK6rO6Bwx3fTltKfUsy")

# for later
# print(re.sub(r'(?m)^\[.*\n?', '', song.lyrics))  # remove square brackets
# preprocessing - remove [Chorus] etc. tags, remove empty lines

genre = "rnb" # one of ['rock', 'pop', 'rnb', 'country']
with open("data/" + genre + "_small.csv") as infile:
    for line in infile:
        line = line.rstrip()
        tokens = line.split(",")
        song_id = tokens[0][1:-1]  # remove surrounding quotations
        artist_name = tokens[1][1:-1]
        track_name = tokens[2][1:-1]

        try:
            song = genius.search_song(track_name, artist_name)
            lyrics = re.sub(r'(?m)^\[.*\n?', '', song.lyrics)
            # only get first 8000 chars if lyrics is longer
            if (len(lyrics) >= 8000):
                lyrics = lyrics[:8000]
            print(lyrics)
            try:
                sql = "INSERT INTO lyrics (id, artist_name, track_name, lyrics, genre) VALUES (%s, %s, %s, %s, %s)"
                val = (song_id, artist_name, track_name, lyrics, genre)
                mycursor.execute(sql, val)
                mydb.commit()
            except Exception as e:
                print("++++++++++++++++++++++ ERROR: Couldn't write lyrics to db ++++++++++++++++++++++")
                print(e)
        except Exception as e:
            print("++++++++++++++++++++++ ERROR: Couldn't get lyrics for " + track_name + " by " + artist_name + "++++++++++++++++++++++")
            print(e)
