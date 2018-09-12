import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

ri = pd.read_csv(
    'C:/Users/Mostafa_2/Desktop/udemy python/data school pandas/using pandas/pycon-2018-tutorial-master/police.csv')
ri.head()
ri.shape
ri.dtypes
ri.isnull().sum()
# now we want to remove the county_name is it doesent contain any data (shape shows 91741 rows and county_name shows 91741 missing value)
# axis =1 means column and can be replaced by axis='columns'
ri.drop('county_name', axis=1, inplace=True)
ri.shape  # 14 column now not 15
# can be done by : ri.dropna(axis=1,how='all')
