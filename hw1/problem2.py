import pandas as pd
# from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
countries=pd.read_csv('data/countries.csv')
print(f'{countries}')
income=pd.read_excel('data/income_per_person_gdppercapita_ppp_inflation_adjusted.xlsx')
print(f'{income.head()}')
print(f'{income.transpose()}')
#----END OF PROBLEM 2a----
year=2000
plt.title('Income per person vs country')
plt.scatter(income.country,income[year])
plt.xlabel('Country')
plt.ylabel('Income per person')
plt.show()
#----END OF PROBLEM 2b----
def merge_by_year(y):
    countries_new=countries.rename(columns={'Country':'country','Region':'region'})
    merged=pd.merge(income[['country',y]],countries_new,on='country')
    return merged[['country','region',y]].rename(columns={y:'income'})
# print(merge_by_year(2000))
#----END OF PROBLEM 2c----

l,u=list(map(int,input('Range: ').split()))
years=np.arange(l,u+1)
for year in years:
    merged=merge_by_year(year)
    plt.title('Average Income per person vs Region for the year: '+str(year))
    regions=merged.region.drop_duplicates()
    incomes=[]
    for i in regions:
        incomes.append(merged.income[merged.region==i].mean())
    plt.tick_params(rotation=90)
    plt.bar(regions,incomes,align='center',alpha=0.5)
    plt.xlabel('Region')
    plt.ylabel('Average Income')
    plt.show()