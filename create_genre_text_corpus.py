import mysql.connector
import re

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="helloworld",
    database="seng474"
)

mycursor = mydb.cursor()

genre="country"
mycursor.execute('SELECT lyrics FROM lyrics WHERE genre="' + genre + '"')

lyrics = mycursor.fetchall()

corpus = []
for lyric in lyrics:
    lyric = lyric[0] # get lyric from tuple of (lyric, )
    lyric = lyric.replace('\n', ' ') # replace all newlines with whitespace
    tokens = lyric.split() # split words on whitespace
    clean_tokens = [t.lower() for t in tokens if re.match(r'[^\W\d]*$', t)] # remove all elements in array which are not alphanumeric
    corpus += clean_tokens

f = open("data/" + genre + "_text_corpus.txt", "a")
f.write(' '.join(corpus))
f.close()