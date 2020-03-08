import pandas as pd
from pandas import DataFrame

df=pd.read_csv('https://grouplens.org/datasets/movielens/25m/',sep='|')
print(df)
