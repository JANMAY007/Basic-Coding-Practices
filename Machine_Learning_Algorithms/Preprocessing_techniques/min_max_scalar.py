import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler

if __name__ == '__main__':
    sns.set(color_codes=True)
    df = pd.DataFrame({
        'x1': np.random.chisquare(8, 1000),
        'x2': np.random.beta(8, 2, 1000) * 40,
        'x3': np.random.normal(50, 3, 1000)
    })
    df.plot.kde()
    plt.show()
    min_max = MinMaxScaler()
    data_tf = min_max.fit_transform(df)
    df = pd.DataFrame(data_tf, columns=['x1', 'x2', 'x3'])
    df.plot.kde()
    plt.show()
