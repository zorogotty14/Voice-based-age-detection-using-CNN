import math
import pandas


triplets_file = 'song.csv'
songs_metadata_file = 'song_data.csv'
song_df_1 = pandas.read_csv(triplets_file,header=None)
print(song_df_1)
song_df_1.columns = ['np','user_id']
song_df_1.drop(columns=['np'])
