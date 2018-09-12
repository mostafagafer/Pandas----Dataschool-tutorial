import pandas as pd

train = pd.read_csv('http://bit.ly/kaggletrain')
train.head()
train['Sex_num'] = train.Sex.map({'female': 0, 'male': 1})
train.loc[0:4, ['Sex', 'Sex_num']]
train['Name_legnth'] = train.Name.apply(len)
train.loc[0:4, ['Sex', 'Name_legnth']]


import numpy as np
train['Fare_ceil'] = train.Fare.apply(np.ceil)
train.loc[0:4, ['Fare', 'Fare_ceil']]


train.Name.str.split(',').head()


def get_element(my_list, position):
    return my_list[position]


train.Name.str.split(',').apply(get_element, position=0).head()


drinks = pd.read_csv('http://bit.ly/drinksbycountry')
drinks.head()
drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis=0)
drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis=1)
drinks.loc[:, 'beer_servings':'wine_servings'].apply(np.argmax, axis=1)

drinks.loc[:, 'beer_servings':'wine_servings'].applymap(float)
