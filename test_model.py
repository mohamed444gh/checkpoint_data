import pandas as pd
import numpy as np
import plotly.express as px
from numpy.ma.core import around
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

data=pd.read_csv("../diabetes (1).csv", sep=",")
print(data.info())
new=data.groupby("Age")[["DiabetesPedigreeFunction","Glucose"]].mean()
print(new.sort_values(by="Age",ascending=True))
fig=px.bar(data,x="Outcome",y="Age",color="Pregnancies")
# fig.show()
tar=data["Outcome"]
feat=data.drop("Outcome", axis=1)
x_train,x_test,y_train,y_test=train_test_split(feat, tar, test_size=0.2, random_state=42)
print(x_train)
print(y_train)
print(x_test)
print(y_test)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)
model = LogisticRegression(max_iter=1000)
for i in range (100):
  model.fit(x_train,y_train)
print(model.coef_)
y_pred=model.predict(x_test)
print(y_pred)
print(y_test.head(15))
print("Accuracy :",around(accuracy_score(y_test, y_pred)*100),"%")
print("Confusion Matrix :")
print(confusion_matrix(y_test, y_pred))


