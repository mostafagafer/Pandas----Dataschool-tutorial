import pandas as pd

# read a dataset of movie reviewers (modifying the default parameter values for read_table)
user_cols = ['user_id', 'age', 'gender', 'occupation', 'zip_code']
users = pd.read_table('http://bit.ly/movieusers', sep='|',
                      header=None, names=user_cols, index_col='user_id')
users.head()
users.shape
users.zip_code.duplicated()  # boleans of true and false
users.zip_code.duplicated().sum()  # trues wil sum to 1 and false will sum to 0
users.duplicated()
users.duplicated().sum()
users.loc[users.duplicated(), :]
users.loc[users.duplicated(keep='first'), :]
users.loc[users.duplicated(keep='last'), :]
users.loc[users.duplicated(keep=False), :]

# toremove the duplicates
users.drop_duplicates().shape  # rows were 943 and now 936 (-7 duplicates)
# rows were 943 and now 936 (-7 duplicates) removed the last
users.drop_duplicates(keep='first').shape
# rows were 943 and now 936 (-7 duplicates) removed the first
users.drop_duplicates(keep='last').shape
users.drop_duplicates(keep=False).shape  # rows were 929 and now 936 (-14 duplicates) removed both


# if we want to consider only tow columns to bo idinticals = duplicates
users.duplicated(subset=['age', 'zip_code']).sum()
# to remove them
users.drop_duplicates(subset=['age', 'zip_code']).shape
