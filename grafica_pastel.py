import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Fastfood.csv')
df10 = df.head(10)

comida = df10['Item']
calorias = df10['Calories']

plt.figure(figsize=(8, 8))
plt.pie(calorias, labels=comida,autopct='%1.1f%%')
plt.title('Porcentaje de calorias en comida rapida')
plt.axis('equal')  

plt.show()

#https://www.kaggle.com/datasets/joebeachcapital/fast-food