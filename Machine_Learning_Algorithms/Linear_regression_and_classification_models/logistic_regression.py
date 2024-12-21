import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
import numpy as np


if __name__ == '__main__':
    X, y = make_blobs(n_features=2, n_samples=1000, cluster_std=2, centers=2)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=10)
    plt.plot()
    plt.show()
    h = .02
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    lr = LogisticRegression()
    lr.fit(X, y)
    Z = lr.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.pcolormesh(xx, yy, Z, cmap='Greens', shading='auto')
    plt.scatter(X[:, 0], X[:, 1], c=y, s=10)
    plt.plot()
    plt.show()
