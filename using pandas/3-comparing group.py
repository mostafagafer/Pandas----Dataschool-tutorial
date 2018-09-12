import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

ri = pd.read_csv(
    'C:/Users/Mostafa_2/Desktop/udemy python/data school pandas/using pandas/pycon-2018-tutorial-master/police.csv')
ri.head()
ri[ri.violation == 'Speeding'].driver_gender.value_counts()
ri[ri.violation == 'Speeding'].driver_gender.value_counts(normalize=True)  # in %
# can be done by
ri[ri.driver_gender == 'M'].violation.value_counts(normalize=True)
ri[ri.driver_gender == 'F'].violation.value_counts(normalize=True)
# in one line code
ri.groupby('driver_gender').violation.value_counts(normalize=True)
