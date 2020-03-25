import pandas as pd
from pandas import DataFrame
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import gather

salaries_df=pd.read_csv("data/Salaries.csv")
teams_df=pd.read_csv("data/Teams.csv")

print(salaries_df.head())
print(teams_df.head())
#----END OF PROBLEM 1a----

salaries_summary_df=salaries_df.groupby(['yearID','teamID'],as_index=False).sum()
print(f"\n\n{salaries_summary_df.head()}")
#----END OF PROBLEM 1b----

merged_df=pd.merge(salaries_summary_df,teams_df,on=['yearID','teamID'])
print(f"\n\n{merged_df.head()}")
#----END OF PROBLEM 1c----


lower,upper=list(map(int,input('Enter range of years to visualize data: ').split()))
years=np.arange(lower,upper+1)
team=input('Enter the teamID whose data is to be visualized: ')

for year in years:
    plt.title('Team: '+team+', Year: '+str(year)+' Wins versus Total Salaries')
    year_df=merged_df[merged_df.yearID==year]
    plt.scatter(year_df.salary/1e6,year_df.W)
    plt.grid()
    plt.xlabel('Total Salary (in millions)')
    plt.ylabel('Wins')
    plt.xlim(0,200)
    plt.ylim(0,200)
    plt.annotate(team,xy=(year_df.salary[year_df.teamID==team]/1e6,year_df.W[year_df.teamID==team]),xytext=(-30,30),textcoords='offset pixels',arrowprops=dict(arrowstyle='->'),bbox=dict(boxstyle='round,pad=0.6',fc='blue',alpha=0.3))
    plt.show()
#---END OF PROBLEM 1d----
