import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = (
    pd.read_csv("dataset/data.csv")
    .replace(r"\r", " ", regex=True)
    .replace(r"\n", "", regex=True)
)
x = "Spending Score (1-100)"
y = "Repayment Score 1-5"
data["credit"] = np.floor(np.log(data[x] * data[y]) * 100)

cities = data["City"].unique()
for i, city in enumerate(cities):
    plt.scatter(
        [i] * data[data["City"] == city].shape[0], data[data["City"] == city]["credit"]
    )
plt.xticks([])
plt.legend(cities, loc=8)
plt.show()
