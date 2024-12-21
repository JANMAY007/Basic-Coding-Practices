import pandas as pd
import csv


if __name__ == '__main__':
    df = pd.read_csv('dataset/test.csv', escapechar='\\', quoting=csv.QUOTE_NONE)
    df = pd.DataFrame(df)
    print(df)
