import pandas as pd
drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()


drinks.continent.head()
drinks.set_index('country', inplace=True)
drinks.head()
drinks.continent.head()  # didn't change

drinks.continent.value_counts()  # it is a Series
drinks.continent.value_counts() .index  # has an index

drinks.continent.value_counts().values  # has a vlues
drinks.continent.value_counts().sort_values()  # to sort the values
drinks.continent.value_counts().sort_index()


# now we add the population of Albania and Andorra
people = pd.Series([3000000, 85000], index=['Albania', 'Andorra'], name='population')
people

drinks.beer_servings*people  # it only * the data of Albania and Andorra cuz they share the same  the index

# if we wanted to add the popluation to our data frame , By concatination
pd.concat([drinks, people], axis=1).head()
