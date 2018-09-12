import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

ri = pd.read_csv(
    'C:/Users/Mostafa_2/Desktop/udemy python/data school pandas/using pandas/pycon-2018-tutorial-master/police.csv')
ri.head()
ri.isnull().sum()
# note thatsearch_type =88545 which is the same of below
ri.search_conducted.value_counts()

ri[ri.search_conducted == False].search_type.value_counts()
# but if we dropedna=False
ri[ri.search_conducted == False].search_type.value_counts(dropna=False)
ri.search_type.value_counts(dropna=False)
# we will found the NaN
