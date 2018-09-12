import pandas as pd
train = pd.read_csv('http://bit.ly/kaggletrain')

train.head()

feature_cols = ['Pclass', 'Parch']
x = train.loc[:, feature_cols]
x.shape
y = train.Survived
y.shape

from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(x, y)
test = pd.read_csv('http://bit.ly/kaggletest')
test.head()

x_new = test.loc[:, feature_cols]
x_new.shape

new_pred_class = logreg.predict(x_new)
new_pred_class
pd.DataFrame({'PassengerId': test.PassengerId, 'Survived': new_pred_class}).set_index('PassengerId')
