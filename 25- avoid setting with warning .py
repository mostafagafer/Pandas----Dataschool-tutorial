import pandas as pd

movies = pd.read_csv('http://bit.ly/imdbratings')
movies.head()
# now we focus oncontenet rating
movies.content_rating.isnull().sum()
movies[movies.content_rating.isnull()]
movies.content_rating.value_counts()  # we find 65 movies not rated

movies[movies.content_rating == 'NOT RATED']
movies[movies.content_rating == 'NOT RATED'].content_rating


import numpy as np

movies[movies.content_rating == 'NOT RATED'].content_rating = np.nan
# it gives a warning
# and the is null is still 3
movies.content_rating.isnull().sum()

# so use .loc method
movies.loc[movies.content_rating == 'NOT RATED', 'content_rating'] = np.nan
movies.content_rating.isnull().sum()  # the is null is now 68 (3 allready nan and 65 of not rated)

#########################

top_movies = movies.loc[movies.star_rating >= 9, :]
top_movies.head()
# suppose we wanted to change duratio of the 1st movie to 150
top_movies.loc[0, 'duration'] = 150
# it will give a warning m but the data are saved
top_movies.head()

# so from now on add .copy()
top_movies = movies.loc[movies.star_rating >= 9, :].copy()
top_movies.head()
top_movies.loc[0, 'duration'] = 150
# now no warning
top_movies.head()
