import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

ufo.head()

ufo.dtypes
ufo.Time.str.slice(-5, -3).astype(int).head()
ufo['Time'] = pd.to_datetime(ufo.Time)
ufo.head()  # now the time formate has changed
ufo.dtypes  # time is datetime64[ns]
# the benifit of datetime64[ns] is
ufo.Time.dt.hour
ufo.Time.dt.weekday_name
ufo.Time.dt.weekday
ufo.Time.dt.dayofyear

pd.to_datetime('1/1/1999')  # creating a time stamp
ts = pd.to_datetime('1/1/1999')
ufo.loc[ufo.Time > ts, :].head()


ufo.Time.max()  # the latest
ufo.Time.min()
ufo.Time.max()-ufo.Time.min()  # bolean

%matplotlib inline
ufo['Year'] = ufo.Time.dt.year
ufo.head()

ufo.Year.value_counts()
ufo.Year.value_counts().sort_index().plot()
