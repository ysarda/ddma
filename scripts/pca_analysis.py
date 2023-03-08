import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

data = (
    pd.read_csv("dataset/data.csv")
    .replace(r"\r", " ", regex=True)
    .replace(r"\n", "", regex=True)
)
contdata = data.iloc[:, [1, 2, 5]].to_numpy()
pca = PCA(n_components=2)
pca.fit(contdata)

cities = data["City"].unique()
for city in cities:
    x = pca.transform(data[data["City"] == city].iloc[:, [1, 2, 5]].to_numpy())
    plt.scatter(x[:, 0], x[:, 1], label=city)
plt.legend(cities)
plt.show()
