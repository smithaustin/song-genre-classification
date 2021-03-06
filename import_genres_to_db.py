import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="helloworld",
  database="seng474"
)

mycursor = mydb.cursor()
with open("data/genres.txt") as infile: # this is the musixmatch file
    for line in infile:
        line = line.strip('\n')
        tokens = line.split("\t")
#         print(tokens)

        # write tokens to db
        sql = "INSERT INTO genres (id, genre) VALUES (%s, %s)"
        val = (str(tokens[0]), str(tokens[1]))
        mycursor.execute(sql, val)

mydb.commit()



# # write to csv
# words = ["\"" + str(i) + "\"" for i in tokens]
# outfile.write(','.join(words))
# outfile.write('\n')