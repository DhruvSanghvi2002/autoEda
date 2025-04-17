import pandas as pd
from scipy.stats import zscore


def detect_outliers(df: pd.DataFrame, method='iqr', threshold=1.5):
    outliers = {}
    numeric_cols = df.select_dtypes(include="number").columns
    for col in numeric_cols:
        if method == 'iqr':
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3-Q1
            lower_bound = Q1-(threshold*IQR)
            upper_bound = Q3+(threshold*IQR)
            outliers[col] = df[(df[col] < lower_bound) | (
                df[col] > upper_bound)].index.tolist()
        elif method == 'zscore':
            z_scores = zscore(df[col])
            outliers[col] = df[(z_scores > threshold) | (
                z_scores < -threshold)].index.tolist()
    return outliers
