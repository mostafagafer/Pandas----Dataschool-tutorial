import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

ri = pd.read_csv(
    'C:/Users/Mostafa_2/Desktop/udemy python/data school pandas/using pandas/pycon-2018-tutorial-master/police.csv')
ri.head()

ri.search_conducted.value_counts(normalize=True)
ri.search_conducted.mean()
ri.groupby('driver_gender').search_conducted.mean()
ri.groupby(['violation', 'driver_gender']).search_conducted.mean()
