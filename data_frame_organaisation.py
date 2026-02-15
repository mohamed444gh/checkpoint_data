import pandas as pd

data = {'Name': ['John', 'Mary', 'Bob', 'Sarah', 'Tom', 'Lisa'], 'Department': ['IT', 'Marketing', 'Sales', 'IT', 'Finance', 'Marketing'], 'Age': [30, 40, 25, 35, 45, 28], 'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female'], 'Salary': [50000, 60000, 45000, 55000, 70000, 55000], 'Experience': [3, 7, 2, 5, 10, 4]}
donner=pd.DataFrame(data)
print(donner)
ligne=donner.iloc[:3]
print("les 3 perimier lingne :\n ",ligne)
mark=donner.loc[donner["Department"]=="Marketing"]
age_gender=donner[["Age","Gender"]].iloc[:3]
print("les 3 premier ligne des age_gender : \n",age_gender)
salair_sex=donner[["Salary","Gender"]].loc[donner["Gender"]=="Male"]
print(salair_sex)



