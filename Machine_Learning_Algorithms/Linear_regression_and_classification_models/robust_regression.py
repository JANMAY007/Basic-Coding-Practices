from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RANSACRegressor
from sklearn.datasets import make_regression
from matplotlib import pyplot as plt
import numpy as np

if __name__ == '__main__':
    n_samples = 1000
    n_outliers = 50
    X, y, coefficient = make_regression(
        n_samples=n_samples,
        n_features=1,
        n_informative=1,
        noise=10,
        coef=True,
        random_state=0
    )
    np.random.seed(0)
    X[:n_outliers] = 3 + 0.5 * np.random.normal(size=(n_outliers, 1))
    y[:n_outliers] = -3 + 10 * np.random.normal(size=n_outliers)
    lr = LinearRegression()
    lr.fit(X, y)
    ransac = RANSACRegressor()
    ransac.fit(X, y)
    plt.scatter(X, y, s=5)
    plt.show()
    ransac_predict = ransac.predict(X)
    lr_predict = lr.predict(X)
    plt.scatter(X, y, s=5, label='data')
    plt.scatter(X, ransac_predict, s=5, label='ransac')
    plt.scatter(X, lr_predict, s=5, label='linear-regression')
    plt.legend()
    plt.show()
