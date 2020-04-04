from sklearn.cluster import KMeans
import numpy as np
import xarray as xr


def cluster_temp_diff(dataset, n_clusters=10):
    # compare wih clustering on relative changes of temperature (difference to temperature of previous year)
    temp = dataset['T2m'].values.copy()
    X_rel = temp.reshape(999, -1).transpose()
    for i in np.arange(1, 999):
        X_rel[:, i] = X_rel[:, i] - X_rel[:, i-1]
    X_rel = X_rel[:, 1:]

    kmeans_rel = KMeans(n_clusters=n_clusters, random_state=0).fit(X_rel)

    return kmeans_rel.labels_.reshape(96, 192)
