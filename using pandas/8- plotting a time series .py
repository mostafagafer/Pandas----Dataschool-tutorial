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
ri.stop_datetime.dt.year
ri.stop_datetime.dt.year.value_counts()

# how does drugs_related_stopchanged by date time
ri.drugs_related_stop.dtypes
ri.drugs_related_stop.mean()

ri.groupby(ri.stop_datetime.dt.hour).drugs_related_stop.mean()
