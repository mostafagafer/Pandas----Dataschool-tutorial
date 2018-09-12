import pandas as pd
ufo = pd.read_csv('http://bit.ly/uforeports')

ufo.tail()
ufo.isnull().tail()  # true if the there is no object
ufo.notnull().tail()  # false if the there is no object

ufo.isnull().sum()
# we founf that there are 25 city with no data
ufo[ufo.City.isnull()]


ufo.shape  # 18241 rows

ufo.dropna(how='any').shape  # 2486 for nulls

ufo.dropna(how='all').shape  # 18241 for nulls becaus state and time has no nulls

# cancel the data if the city or shape reported is null
ufo.dropna(subset=['City', 'Shape Reported'], how='any').shape


ufo['Shape Reported'].value_counts()  # it allready drope null value
ufo['Shape Reported'].value_counts(dropna=False)  # adding the missing values

# to fill the data for example of the shape reported
ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)
ufo['Shape Reported'].value_counts()  # null value changed to  VARIOUS
