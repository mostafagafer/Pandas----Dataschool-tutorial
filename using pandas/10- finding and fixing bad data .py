import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

ri = pd.read_csv(
    'C:/Users/Mostafa_2/Desktop/udemy python/data school pandas/using pandas/pycon-2018-tutorial-master/police.csv')
ri.tail(50)

ri.stop_duration.value_counts()
ri.stop_duration.value_counts(dropna=False)
ri.loc[(ri.stop_duration == '1') | (ri.stop_duration == '2'), 'stop_duration'] = 'NaN'
ri.stop_duration.value_counts()
ri.stop_duration.value_counts(dropna=False)


import numpy as np
ri.loc[ri.stop_duration == 'NaN', 'stop_duration'] = np.nan
ri.stop_duration.value_counts()
ri.stop_duration.value_counts(dropna=False)
