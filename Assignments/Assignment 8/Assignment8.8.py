from matplotlib import pyplot as plt 
import numpy as np
import pandas as pd 

width = 0.2
path =  "D:\\Coding\\Python\\Python-Programing\\Assignments\\Assignment 8\\crime_data.csv"

with open(path,'r') as file:
    data =  pd.read_csv(file)
    Country = data['Country']
    Murder = data['Murder']
    Assault = data['Assault']
    UrbanPop = data['UrbanPop']
    Rape = data['Rape']

C = np.arange(len(Country))

plt.bar(C+0.0,Murder,width,color = 'r')
plt.bar(C+0.2,Assault,width,color = 'g')
plt.bar(C+0.4,UrbanPop,width,color = 'b')
plt.bar(C+0.6,Rape,width,color = 'c')

plt.xticks(rotation =63)
plt.xticks(C,Country)


plt.xlabel('Country Name')
plt.ylabel('Crime Rate')
plt.title('Crime Data')

plt.show()