import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("C:/Users/mvb02/Desktop/Python/Projetos/Projeto-Dio/movies.csv")
filme = list(df["Name"])
media = list(df["Vote_average"])
new_filme = []
new_media = []
for n in range(10):
    i = np.random.randint(0, len(filme))
    new_filme.append(filme[i])
    new_media.append(media[i])

plt.rcParams['font.family'] = 'Arial'
plt.subplots_adjust(left = 0.4, right= 0.9)
plt.scatter(new_media, new_filme)
plt.show()