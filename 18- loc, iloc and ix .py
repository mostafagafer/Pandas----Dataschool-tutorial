import pandas as pd

ufo = pd.read_csv('http://bit.ly/uforeports')
ufo.head(3)

# selecting things by label: .loc[waht row i want, what column i want]
ufo.loc[0, :]
ufo.loc[[0, 1, 2], :]
# or by
ufo.loc[0:2, :]
# if i need all the column leave it empty
ufo.loc[0:2]


# column
ufo.loc[:, 'City']
# to column needed
ufo.loc[:, ['City', 'State']]
# or by rane [City:State]--> city through state
ufo.loc[:, 'City': 'State']


# this can be acived by drop:
ufo.drop('Time', axis=1)


########
ufo[ufo.City == 'Oakland']
# same results
ufo.loc[ufo.City == 'Oakland', :]


# IlOC :integer position
ufo.iloc[:, [0, 3]]
ufo.iloc[:, 0: 4]
ufo.iloc[0:3, :]

# now we can chose different column by
ufo[['City', 'State']]
ufo.loc[:, ['City', 'State']]


drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.set_index('country', inplace=True)
drinks.head()

# if we want Albani beer_servings
drinks.ix['Albania', 0]
# or
drinks.ix[1, 'beer_servings']
# or by compining both
drinks.ix['Andorra', 'spirit_servings']
# or by
drinks.ix['Albania': 'Andorra', 0:2]
