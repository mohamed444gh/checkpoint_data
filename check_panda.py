import pandas as pd
# question 1:
data = pd.read_csv("../STEG_BILLING_HISTORY.csv", sep=",")
clien0=data.iloc[:10,:]
# question 2:
print("question 2:\n")
print(type(clien0))
# question 3 :
print("question 3:\n")
print(data.info())
# question 4 :
print("question 4:\n")
print(data.isna().sum())
# question 5 :
print("question 5:\n")
#data_cleaning=data.isna()#on supprimer toot les nan parceque la base de donner est tres grand
#or
data_cleaning=data.fillna(data.isna().median()) #on remplace toot les nan par le median
print(data_cleaning.isnull().sum())
#question 6 :
print("question 6:\n")
print(data.describe())
# question 7 :
print("question 7:\nmethode 1 :\n")
#mathode 1:
new = data.loc[data["client_id"]== "train_Client_0"]
print(new)
#methode 2 :
print("question 7:\nmethode 2 :\n")
new=data.query("client_id == 'train_Client_0'")
print(new)
#question 8 :
print("question 8:\n")
col_coder = pd.get_dummies(data["counter_type"],columns=["counter_type"])
print(col_coder)
#question 9 :
print("question 9:\n")
final_data=data.drop("counter_statue",axis=1)
print(final_data.info())
