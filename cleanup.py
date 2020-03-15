import pandas as pd
from pandas import DataFrame

fs=open('ratings.csv','r',encoding='ISO-8859-1')
fout=open('ratings_cleaned.csv','w')
data=""
for line in fs:
    c=0
    for i in range(len(line)):
        if line[i]=='|':
            c+=1
        if c==5:
            data+=(line[:i]+'\n')
            break
fout.write(data)
