fam ={
    "Zhulduz":49,
    "Aruzhan":11,
    "Mama":73
}
print(fam)
fam_B={
    'Aliya': 47
}
fam.update(fam_B)
famG={"Gena":46}
fam.update(famG)
print(fam)
fam_T=("Alma",50)
fam["hello"]= 1
fam["hello1"] = (1, 2, 3)
# fam.update(fam_T)
# не смогла добавить элемент типа tuple
print(fam_T)
user=[]
key='Mama'
if key in fam:
    user=fam[key]
print(user)
key='Gena'
if key in fam:
    del fam[key]
print(fam)
for key in fam:
    print(key,' - ',fam[key])

