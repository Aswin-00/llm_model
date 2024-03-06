
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

from sklearn.linear_model import LinearRegression


dataset=pd.read_csv('SD.csv')

X = dataset.iloc[:, 0:1].values
y = dataset.iloc[:, 1:2].values

imputer=SimpleImputer(missing_values=np.NaN,strategy='mean')
X1=imputer.fit_transform(X)
y1=imputer.fit_transform(y)

X_train,X_test,y_train,y_test=train_test_split(X1,y1,test_size=0.3, random_state=0)


regressor=LinearRegression()
regressor.fit(X_train,y_train)

y_pred=regressor.predict(X_test)

regressor.score(X1,y1)


def predo(value):
    salary=int(regressor.predict([[value]]))
    return salary


