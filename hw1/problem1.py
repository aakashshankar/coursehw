import pandas as pd
from pandas import DataFrame
import gather

salaries_df=pd.read_csv("Salaries.csv")
teams_df=pd.read_csv("Teams.csv")

print(salaries_df.head())
print(teams_df.head())
#----END OF PROBLEM 1a----

salaries_summary_df=salaries_df.groupby([salaries_df['teamID'],salaries_df['yearID']]).sum()
print(f"\n\n{salaries_summary_df.head()}")
#----END OF PROBLEM 1b----

merged_df=pd.merge(salaries_df,teams_df,on=['teamID','yearID'])
merged_grouped_df=merged_df.groupby([merged_df.teamID,merged_df.yearID]).sum()
print(f"\n\n{merged_grouped_df.head()}")
#----END OF PROBLEM 1c----


