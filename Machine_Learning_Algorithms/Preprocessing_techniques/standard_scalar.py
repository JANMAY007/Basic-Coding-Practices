import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler


if __name__ == '__main__':
    sns.set(color_codes=True)
    df = pd.DataFrame({
        'x1': np.random.normal(0, 2, 10000),
        'x2': np.random.normal(5, 3, 10000),
        'x3': np.random.normal(-5, 5, 10000)
    })
    df.plot.kde()
    plt.show()
    standard_scalar = StandardScaler()
    data_tf = standard_scalar.fit_transform(df)
    df = pd.DataFrame(data_tf, columns=['x1', 'x2', 'x3'])
    df.plot.kde()
    plt.show()
