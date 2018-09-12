import pandas as pd

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks

pd.get_option('display.max_rows')
# it gives 60 rows 30 head and 30 tail

pd.set_option('display.max_rows', None)

# to back to normal
pd.reset_option('display.max_rows')
drinks

# and for the columns
pd.get_option('display.max_columns')
# and the set and reset are the same


train = pd.read_csv('http://bit.ly/kaggletrain')
train.head()
# we found the there are som .... that mean long name
pd.get_option('display.max_colwidth')
# it gives 50 character to be displayed
# the same for set and reset :D

# now we note that the fair is 4 digits
pd.get_option('display.precision')  # 6
# the same with set and reset


pd.describe_option('rows')

# this is how to reset all things you modified
pd.reset_option('all')
# gives a warning but its okay
