-- create_schema.txt

-- Issue a pre-emptive rollback (to discard the effect of any active transaction) --
rollback;

-- must drop tables which reference other tables via foreign key first
drop table if exists words;
drop table if exists genres;
drop table if exists lyrics;

create table words(
     id varchar(50) primary key,
     artist_name varchar(255) not null,
     track_name varchar(255) not null,
     mxm_id varchar(50) not null,
     mxm_artist_name varchar(255) not null,
     mxm_track_name varchar(255) not null
);

create table genres(
   id varchar(50) primary key,
   genre varchar(100) not null
);

create table lyrics(
   id varchar(50) primary key,
   artist_name varchar(255) not null,
   track_name varchar(255) not null,
   lyrics varchar(8000) not null,
   genre varchar(100) not null
);

create table audio_features(
   id varchar(50) primary key,
   analysis_sample_rate integer,
   danceability float,
   duration float,
   end_of_fade_in float,
   energy float,
   music_key integer,
   key_confidence float,
   loudness float,
   mode float,
   mode_confidence float,
   start_of_fade_out float,
   tempo float,
   time_signature integer,
   time_signature_confidence float
);