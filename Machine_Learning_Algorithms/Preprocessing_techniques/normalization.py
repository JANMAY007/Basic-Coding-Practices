import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import Normalizer

if __name__ == '__main__':
    sns.set(color_codes=True)
    df = pd.DataFrame({
        'x1': np.random.randint(-100, 100, 1000).astype(float),
        'y1': np.random.randint(-80, 80, 1000).astype(float),
        'z1': np.random.randint(-150, 150, 1000).astype(float),
    })
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(df.x1, df.y1, df.z1)
    plt.show()
    normalizer = Normalizer()
    data_tf = normalizer.fit_transform(df)
    df = pd.DataFrame(data_tf, columns=['x1', 'y1', 'z1'])
    ax = plt.axes(projection='3d')
    ax.scatter3D(df.x1, df.y1, df.z1)
    plt.show()
