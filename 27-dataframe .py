import pandas as pd

df = pd.DataFrame({'id': [100, 101, 102], 'color': ['red', 'blue', 'red']},
                  columns=['id', 'color'], index=['a', 'b', 'c'])


pd.DataFrame([[100, 'red'], [101, 'blue'], [102, 'red']],
             columns=['id', 'color'], index=['a', 'b', 'c'])


import numpy as np
arr = np.random.rand(4, 2)
arr
pd.DataFrame(arr, columns=['one', 'two'])

pd.DataFrame({'student': np.arange(100, 110, 1), 'test': np.random.randint(60, 101, 10)})


# Adding a series to a data frame

s = pd.Series(['round', 'square'], index=['c', 'b'], name='shape')
s
pd.concat([df, s], axis=1)
