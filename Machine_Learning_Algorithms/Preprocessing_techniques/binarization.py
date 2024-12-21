from sklearn.preprocessing import Binarizer
import numpy as np


if __name__ == '__main__':
    X = np.array([[1., -1.,  2.],
                  [2.,  0.,  0.],
                  [0.,  1., -1.]])
    binarizer = Binarizer()
    data_tf = binarizer.fit_transform(X)
    print(data_tf)
