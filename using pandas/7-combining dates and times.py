import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

ri = pd.read_csv(
    'C:/Users/Mostafa_2/Desktop/udemy python/data school pandas/using pandas/pycon-2018-tutorial-master/police.csv')
ri.head()
ri.search_type.value_counts(dropna=False)
# which year has the least no. of STOPS
ri.stop_date.str.slice(0, 4).value_counts()


# or can be done by
combined = ri.stop_date.str.cat(ri.stop_time, sep=' ')
combined
ri['stop_datetime'] = pd.to_datetime(combined)
ri.dtypes  # stop_datetime is a datetime64[ns]
ri.stop_datetime.dt.year
ri.stop_datetime.dt.year.value_counts()
