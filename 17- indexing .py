import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')

drinks.head()

# to check what is your index
drinks.index

# to check what is your coulmns
drinks.columns


# to check the data by continent south america
drinks[drinks.continent == 'South America']


# now set the index to the country:
drinks.set_index('country', inplace=True)

drinks.head()

# the name country is hanged , so :
drinks.index.name = None
drinks.head()


# now check what is your index---> is country
drinks.index

# now check what is your coulmns---> no country here
drinks.columns


# now if we want to check peer serving in brasil we can use loc
drinks.loc['Brazil', 'beer_servings']


# if you want to back to old where country is colmn and normal indexing
drinks.index.name = 'country'
drinks.reset_index(inplace=True)
drinks.head()


# now check the describe method
drinks.describe()  # it is a data frame and has an index
drinks.describe().index  # these are index
drinks.describe().columns  # these are the colm
# so we can treat it with loc
drinks.describe().loc['mean', 'beer_servings']
