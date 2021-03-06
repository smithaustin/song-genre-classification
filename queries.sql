SELECT * FROM words JOIN genres ON words.id = genres.id and genres.genre='Rock' limit 10;

SELECT * FROM words JOIN genres ON words.id = genres.id and genres.genre='Jazz' limit 10 into outfile "/usr/local/mysql/data/test.txt" FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';

-- create csv of id, artist name and track name of length 10
SELECT artist_name, track_name FROM words JOIN genres ON words.id = genres.id and genres.genre='Country' limit 2000 into outfile "/usr/local/mysql/data/country.csv" FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';