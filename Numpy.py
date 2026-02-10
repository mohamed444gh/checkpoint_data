import numpy as np
ne=nm=""
while True:
    try:
       ne=int(input("donner le nb des etudient : "))
       nm=int(input("donner le nb des matier : "))
       break
    except ValueError:
        print("svp donner nb entier exp: 1,2,3,4,...")
tab = np.random.randint(1,4,size=(int(ne),int(nm)))
print(tab)
for i in range (ne):
    for j in range (nm):
        tab[i,j]=int(input("donner le note du matiere {} de letudient {} :".format(j+1,i+1)))
        print(tab[i,j])
note=[]
for i in range (ne):
    note.append(int(np.sum(tab[i,:])))
p=[]
for i in note :
    p.append((i*10)/nm)
print(p)
for i in p:
    if i>=90:
        print("leleve {} de mention A+".format(p.index(i)+1))
    elif i>=80:
        print("leleve {} de mention A".format(p.index(i)+1))
    elif i>=70:
        print("leleve {} de mention B+".format(p.index(i)+1))
    elif i>=60:
        print("leleve {} de mention B".format(p.index(i)+1))
    elif i>=50:
        print("leleve {} de mention C".format(p.index(i)+1))
    else :
        print("leleve {} de mention F".format(p.index(i)+1))