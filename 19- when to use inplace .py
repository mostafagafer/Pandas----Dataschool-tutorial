import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')

ufo.shape
ufo.head()
ufo.drop('City', axis=1).head()

# city column did't gone
ufo.head()
ufo.drop('City', axis=1, inplace=True)
ufo.head()


######
ufo.dropna(how='any')
ufo.dropna(how='any').shape
# now yet inplaced
ufo.shape


# can be done by assigin for a variable
