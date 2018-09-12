import pandas as pd
movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()
movies.dtypes

# for checking most common
movies.genre.describe()

# for checking how many of each one
movies.genre.value_counts()
# normalized:
movies.genre.value_counts(normalize=True)

# to see the unique value
movies.genre.unique()


# to see how many unoque
movies.genre.nunique()

# cross tab between genre and rating:
pd.crosstab(movies.genre, movies.content_rating)


#   numeric coulmn such as duration :
movies.duration.describe()
movies.duration.mean()
movies.duration.value_counts()


# ploting
%matplotlib inline
movies.duration.plot(kind='hist')
movies.genre.value_counts().plot(kind='bar')
