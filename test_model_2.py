import pandas as pd
import numpy as np
import plotly.express as px
from numpy.ma.core import around
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, cross_val_score

iris = load_iris()
data=pd.DataFrame(iris.data,columns=iris.feature_names)
print(data.head())
print(data.info())
print(data.describe())
fig=px.bar(data,x="sepal length (cm)",y="sepal width (cm)",color="petal length (cm)")
# fig.show()
model = LinearRegression()
fut=data.drop("petal width (cm)", axis=1)
tar=data["petal width (cm)"]
x_train,x_test,y_train,y_test = train_test_split(fut,tar,test_size=0.2,random_state=42)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
print("MSE =", mean_squared_error(y_test, y_pred))
print("R2 =", r2_score(y_test, y_pred))
scor = cross_val_score(model, data, tar, cv=5)
print(scor)
print("rendoment 2 : ",scor.mean())