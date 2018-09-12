import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

ri = pd.read_csv(
    'C:/Users/Mostafa_2/Desktop/udemy python/data school pandas/using pandas/pycon-2018-tutorial-master/police.csv')
ri.head()
ri.search_type.value_counts(dropna=False)
# how often driver frisked
ri['frisk'] = ri.search_type.str.contains('Protective Frisk')
ri.frisk.value_counts()
ri.frisk.value_counts(dropna=False)
ri.frisk.sum()
ri.frisk.mean()
