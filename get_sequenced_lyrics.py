import lyricsgenius
import re

genius = lyricsgenius.Genius("qi60kr-M7_fI1jM9eN530XOblD2nEO9Jviyp4OCFRrcQSbALuO9BSxeWNKrWtnlh")

with open("rock_small.csv") as infile:
    for line in infile:
        tokens = line.split(",")
        artist = tokens[0]
        artist = artist[1:-1]
        track = tokens[1]
        track = track[1:-1]

        print([artist, track])

        try:
            song = genius.search_song(track, artist)
            # format lyrics here
            print(re.sub(r'(?m)^\[.*\n?', '', song.lyrics)) # remove square brackets
            # TODO: write lyrics to output format
            # IMPORTANT - how to preprocess / format lyrics for best sequenced lyrics analysis
            # ie. strip lines so its just one long text string for each song?
        except:
            print("Couldn't get lyrics for " + track + " by " + artist)
