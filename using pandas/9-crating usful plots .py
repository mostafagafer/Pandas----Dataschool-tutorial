import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

ri = pd.read_csv(
    'C:/Users/Mostafa_2/Desktop/udemy python/data school pandas/using pandas/pycon-2018-tutorial-master/police.csv')
ri.tail(50)

combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')
combined
ri['stop_datetime'] = pd.to_datetime(combined)
ri.dtypes  # stop_datetime is a datetime64[ns]
ri.stop_datetime.dt.hour.value_counts()
# if we applied .plot() it will give a wrong plot
# so need to sort values
ri.stop_datetime.dt.hour.value_counts().sort_values()
ri.stop_datetime.dt.hour.value_counts().sort_index()
ri.stop_datetime.dt.hour.value_counts().sort_index().plot()
###
# or by
ri[(ri.stop_datetime.dt.hour > 4) & (ri.stop_datetime.dt.hour < 22)].shape  # =68575 row out of
ri.shape  # =91741 rows

# or by
ri.count()
ri.stop_date.count()
ri.groupby(ri.stop_datetime.dt.hour).stop_date.count().plot()
