import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="helloworld",
  database="seng474"
)

mycursor = mydb.cursor()
with open("data/bag_of_words.txt") as infile: # this is the musixmatch file
    for line in infile:
        line = line.strip('\n')
        tokens = line.split("<SEP>")

        # write tokens to db
        sql = "INSERT INTO words (id, artist_name, track_name, mxm_id, mxm_artist_name, mxm_track_name) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (str(tokens[0]), str(tokens[1]), str(tokens[2]), str(tokens[3]), str(tokens[4]), str(tokens[5]))
        mycursor.execute(sql, val)
        mydb.commit()



# # write to csv
# words = ["\"" + str(i) + "\"" for i in tokens]
# outfile.write(','.join(words))
# outfile.write('\n')