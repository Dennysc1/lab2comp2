import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('PS4.csv')
df10 = df.head(6)
juego = df10['Game']
año = df10['Year']

plt.plot(juego,año, color='green')
plt.xlabel('Juegos')
plt.ylabel('Año')
plt.title('año de salida de juegos PS4') 
plt.tight_layout()

plt.show()