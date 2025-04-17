import pandas as pd


def check_class_imbalance(df: pd.DataFrame, target_col: str):
    class_counts = df[target_col].value_counts(normalize=True)
    imbalance = any(class_counts > 0.2)
    return class_counts.to_dict(), imbalance
