import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

ri = pd.read_csv(
    'C:/Users/Mostafa_2/Desktop/udemy python/data school pandas/using pandas/pycon-2018-tutorial-master/police.csv')
ri.head()
ri.shape
ri.dtypes
ri.isnull().sum()


ted = pd.read_csv(
    'C:/Users/Mostafa_2/Desktop/udemy python/data school pandas/using pandas/pycon-2018-tutorial-master/ted.csv')
ted.head()
ted.shape
