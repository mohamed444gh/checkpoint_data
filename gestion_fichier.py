import numpy as np
file=open("Loan_prediction_dataset.csv")
data=np.genfromtxt(file,delimiter=",")
amount=data[:,8]
filtrer=np.isnan(amount)
result={"moyen amount :":np.mean(filtrer),"amount median : ":np.median(filtrer),"emount ecartype : ":np.std(filtrer)}
for x,y in result.items():
    print(x+": "+str(y))




