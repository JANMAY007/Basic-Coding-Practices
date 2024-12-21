import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import RobustScaler

if __name__ == '__main__':
    sns.set(color_codes=True)
    df = pd.DataFrame({
        'x1': np.concatenate([np.random.normal(20, 1, 1000), np.random.normal(1, 1, 25)]),
        'x2': np.concatenate([np.random.normal(30, 1, 1000), np.random.normal(50, 1, 25)]),
    })
    df.plot.kde()
    plt.show()
    robust_scaler = RobustScaler()
    data_tf = robust_scaler.fit_transform(df)
    df = pd.DataFrame(data_tf, columns=['x1', 'x2'])
    plt.show()
