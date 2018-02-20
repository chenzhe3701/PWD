from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
import scipy.io as spio

mat = spio.loadmat('D:\p\m\DIC_Analysis\grain_195.mat')
data = mat['data_t']

range_n_clusters = [2, 3, 4, 5, 6]

for nCluster in range_n_clusters:
    clusterer = KMeans(n_clusters=nCluster)
    idx = clusterer.fit_predict(data)

    silhouetteAvg[nCluster] = silhouette_score(data,idx)