import pandas as pd
data=pd.read_csv('results2.csv')
header=list(data.columns)
ds=data.values.tolist()
dict={}
for i in ds:
    dict[i[0]]=0
file=open('chi_so_lon_nhat.txt','w')
for i in range(1,141):
    Max=0
    s=''
    for j in ds:
        if j[i]>Max:
            Max=j[i]
            s=j[0]
    file.write(header[i]+':'+s+'('+str(Max)+')\n')
    if i>1:dict[s]+=1
Max=max(dict.values())
file.write('\n\nDoi phong do tot nhat la: ')
for i in dict:
    if Max==dict[i]:
        file.write(i+', ')