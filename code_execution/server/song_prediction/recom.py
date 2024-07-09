
import math as mt
import pandas
from sklearn.model_selection import train_test_split
from .Recom import Recommenders
import numpy as np
from scipy.sparse import csc_matrix
from sparsesvd import sparsesvd
triplets_file = 'C:\\Users\\gotty\\Desktop\\project\\myenv\\server\\song_prediction\\Recom\\song.csv'
songs_metadata_file = 'C:\\Users\\gotty\\Desktop\\project\\myenv\\server\\song_prediction\\Recom\\song_data.csv'
song_df_1 = pandas.read_table(triplets_file,header=None,sep='\t')

song_df_1.columns = ['user_id', 'song_id', 'listen_count']

song_df_2 =  pandas.read_csv(songs_metadata_file)
song_df = pandas.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")
song_grouped = song_df.groupby(['song_id']).agg({'listen_count': 'count'}).reset_index()
grouped_sum = song_grouped['listen_count'].sum()
song_grouped['percentage']  = song_grouped['listen_count'].div(grouped_sum)*100
song_grouped.sort_values(['listen_count', 'song_id'], ascending = [0,1])


train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)

def recommend_songs(user_id,age):
	pm = Recommenders.popularity_recommender_py()
	pm.create(train_data, 'user_id', 'song_id',age)
	return pm.recommend(user_id)
# recom=recommend_songs('b80344d063b5ccb3212f7pg6538f3d9e43d87dca9e',25)
# print(recom)
# recom_list = recom.values.tolist()
# print(recom_list)
# print(type(recom_list))
