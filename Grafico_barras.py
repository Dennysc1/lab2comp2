
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("steam-200k.csv")
cantidad =df["purchase"].value_counts()
colores=["blue","yellow","green","orange","red","gray","purple","black"]
cantidad.plot(kind="bar", color=colores)
plt.xlabel("tipo de review")
plt.ylabel("Cantidad ")
plt.show()
#https://www.kaggle.com/datasets/tamber/steam-video-games