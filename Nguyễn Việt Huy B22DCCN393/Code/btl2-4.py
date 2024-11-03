import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("results2.csv")
header=list(data.columns)
for i in range(1,len(header)):
    plt.hist(data[header[i]],bins=10,color='skyblue',edgecolor='black')
    plt.title('Bảng '+ header[i])
    plt.xlabel(header[i])
    plt.ylabel('Mức độ')
    plt.show()