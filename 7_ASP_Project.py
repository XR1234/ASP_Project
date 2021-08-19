import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Visitors:
    dataframe = pd.read_excel('IMVA.xls', sheet_name = 'IMVA')

    dataframe2 = dataframe[['Periods', 'Belgium & Luxembourg', 'Denmark', 'Finland', 'France', 'Germany',
              'Italy', 'Netherlands', 'Norway', 'Rep Of Ireland',
              'Russian Federation', 'Spain', 'Sweden', 'Switzerland',
              'United Kingdom']]
    print(dataframe2.columns)

    new = dataframe2['Periods'].str.split(' ', n=1, expand=True)
    dataframe2 = dataframe2.assign(Year=new[0])

    dataframe2['Year'] = pd.to_numeric(dataframe2['Year'])
    pd1 = dataframe2['Year'].dtypes
    print("****** first & last 3 years dataframe ******")
    #print(dataframe2.drop(['Periods'], axis=1))
    dataframe3 = dataframe2[(dataframe2['Year'] >= 1988) & (dataframe2['Year'] <= 1997)]
    print(dataframe3)
    print(dataframe3.head(3))
    print(dataframe3.tail(3))

#dataframe4 = dataframe3[[ 'Belgium & Luxembourg', 'Denmark', 'Finland', 'France', 'Germany',
       #'Italy', 'Netherlands', 'Norway', 'Rep Of Ireland',
       #'Russian Federation', 'Spain', 'Sweden', 'Switzerland',
       #'United Kingdom']]

dataframe4 = dataframe3[['Belgium & Luxembourg', 'Denmark', 'Finland', 'France', 'Germany',
                        'Italy', 'Netherlands', 'Norway', 'Rep Of Ireland',
                        'Russian Federation', 'Spain', 'Sweden', 'Switzerland',
                        'United Kingdom']]

print('****** dataframe4 *********')
print(dataframe4)

print('******** sorted ******')

dataframe5 = dataframe4.replace(',', '', regex=True)
dataframe6 = dataframe5.replace('na', '0', regex=True)
print('******** dataframe5 ******')
print(dataframe6)

dataframe7 = dataframe6.astype(int)
print(dataframe7.dtypes)
psNotSorted=dataframe7.sum()
psSorted = dataframe7.sum().sort_values(ascending=False)
print('******** sorted ******')
print(psSorted)

allCountries = psNotSorted
print('****** Top 3 countries ********')

top3countries = psSorted.head(3)
print(top3countries)
total=top3countries.values.sum()
mean=round(top3countries.values.mean(),2)

print("The total no. of visitors for the top 3 countries is ",total)
print("The mean value for the top 3 countries is ",mean)