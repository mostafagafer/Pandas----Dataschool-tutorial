import pandas as pd

train = pd.read_csv('http://bit.ly/kaggletrain')
train.head()

train['Sex_male'] = train.Sex.map({'female': 0, 'male': 1})
train.head()

# or by
pd.get_dummies(train.Sex)
pd.get_dummies(train.Sex).iloc[:, 1:]
pd.get_dummies(train.Sex, prefix='Sex').iloc[:, 1:]


# for more than 2 data
train.Embarked.value_counts()
pd.get_dummies(train.Embarked, prefix='Embarked')
pd.get_dummies(train.Embarked, prefix='Embarked').iloc[:, 1:]
Emparked_dummies = pd.get_dummies(train.Embarked, prefix='Embarked').iloc[:, 1:]
train = pd.concat([train, Emparked_dummies], axis=1)
train.head()
