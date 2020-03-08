import pandas as pd
from pandas import DataFrame
names=['user_id','age','sex','occupation','zip code']
df=pd.read_csv('http://files.grouplens.org/datasets/movielens/ml-100k/u.user',sep='|',names=names)
print(df)
print(df.head())
