import mysql.connector
import pandas as pd
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="songGenre"
)

import h5py

def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)
    return None

base = "C:\\Users\\Austin\\Documents\\SENG474\\millionsongsubset\\MillionSongSubset"
filenames = []

mycursor = mydb.cursor()

mycursor.execute('SELECT id FROM genres')
filenames = mycursor.fetchall()

# filenames = ["C:\\Users\\Austin\\Documents\\SENG474\\millionsongsubset\\MillionSongSubset\\A\\A\\A\\TRAAAAW128F429D538.h5"]
# filenames = ["TRAAAAW128F429D538.h5"]
# print(filenames)
print(len(filenames))

for filename in filenames[0:10000]:
    path = find_file(filename[0] + ".h5", base)
    if path is None:
        continue
    print(filename)
    with h5py.File(path, "r") as f:
        # Get the data
        data_keys = [
            "track_id",
            "analysis_sample_rate",
            "danceability",
            "duration",
            "end_of_fade_in",
            "energy",
            "key",
            "key_confidence",
            "loudness",
            "mode",
            "mode_confidence",
            "start_of_fade_out",
            "tempo",
            "time_signature",
            "time_signature_confidence"
        ]
        id = f['analysis']['songs'][data_keys[0]][0].decode("ascii")
        values = [str(f['analysis']['songs'][k][0]) for k in data_keys]
        data_keys[0] = 'id'
        values[0] = id
        data_keys[6] = 'music_key'
        
        # for i, k in enumerate(data_keys):
        #     print(f"{k}: {values[i]}")
        
        names = ",".join(data_keys)
        place_holders = ",".join(["%s" for i in range(len(data_keys))])
        sql = f"INSERT INTO audio_features ({names}) VALUES ({place_holders})"
        # print(sql)
        mycursor.execute(sql, values)

mydb.commit()

# store = pd.HDFStore(filename)
# df = pd.DataFrame(store)

# import hdf5_getters
# h5 = hdf5_getters.open_h5_file_read(filename)
# duration = hdf5_getters.get_duration(h5)
# print(duration)
# h5.close()