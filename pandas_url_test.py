import pandas as pd
from pandas import DataFrame
movie_cols=['movie_id', 'title', 'release_date','video_release_date', 'imdb_url']
movies=pd.read_csv('ratings_cleaned.csv',sep='|',names=movie_cols,encoding='utf-8')
print(movies)
rating_cols=['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings=pd.read_csv('http://files.grouplens.org/datasets/movielens/ml-100k/u.data',sep='\t',names=rating_cols)
print(ratings)
ratings.merge(movies, on='movie_id')
avg_rating_per_movie=(ratings['rating'].groupby(ratings['movie_id'])).mean()
print(avg_rating_per_movie.max())
print(ratings)
