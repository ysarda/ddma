import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

data = (
    pd.read_csv("dataset/data.csv")
    .replace(r"\r", " ", regex=True)
    .replace(r"\n", "", regex=True)
)
x = "Spending Score (1-100)"
y = "Repayment Score 1-5"
sz = "Annual Revenue (k$)"


cities = data["City"].unique()
for city in cities:
    plt.scatter(data[data["City"] == city][x], data[data["City"] == city][sz])
plt.legend(cities)
plt.xlabel(x)
plt.ylabel(sz)
plt.show()

rpscore = data[y].unique()
for score in rpscore:
    plt.scatter(data[data[y] == score][x], data[data[y] == score][sz])
plt.legend(rpscore)
plt.xlabel(x)
plt.ylabel(sz)
plt.show()
