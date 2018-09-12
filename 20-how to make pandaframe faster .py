import pandas as pd


drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()
drinks.info()  # take about 7.6 + kb
drinks.info(memory_usage='deep')  # take19.9 kb
drinks.memory_usage()  # gives every one how many bites
drinks.memory_usage(deep=True)  # gives the actual every one how many bites
drinks.memory_usage(deep=True).sum()  # sum=20 as seen in line 7


# assigning unique column to a category
drinks['continent'] = drinks.continent.astype('category')
drinks.dtypes  # now continent is a category
drinks.continent.cat.codes.head()
drinks.memory_usage(deep=True)

drinks['country'] = drinks.continent.astype('category')
drinks.memory_usage(deep=True)

df = pd.DataFrame({'ID': [100, 101, 102, 103], 'quality': [
                  'good', 'very good', 'good', 'excellent']})
df

df.sort_values('quality')
df['quality'] = df.quality.astype(
    'category', categories=['good', 'very good', 'excellent'], ordered=True)
df.quality
# now we can sort them
df.sort_values('quality')
df.loc[df.quality > 'good', :]
