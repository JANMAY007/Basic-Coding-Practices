from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression


if __name__ == '__main__':
    X, Y = make_regression(n_features=1, noise=10, n_samples=1000)
    lr = LinearRegression()
    lr.fit(X, Y)
    print(lr.coef_)
    print(lr.intercept_)
    predicted = lr.predict(X)
    plt.scatter(X, Y, label='Training')
    plt.scatter(X, predicted, label='Predicted')
    plt.xlabel("Feature-x")
    plt.ylabel("Target-Y")
    plt.legend()
    plt.show()
