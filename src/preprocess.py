import pandas as pd
import numpy as np

def clean_data(df):
    df = df.copy()

    df = df.drop_duplicates()
    df = df.dropna()

    df = df[df["TotalQuantity"] > 0]
    df = df[df["TotalPurchaseDollars"] > 0]
    df = df[df["Freight"] >= 0]

    return df


def feature_engineering(df):
    df = df.copy()

    df["FreightPerUnit"] = df["Freight"] / df["TotalQuantity"]
    df["PurchaseCostPerUnit"] = df["TotalPurchaseDollars"] / df["TotalQuantity"]

    # Simple risk label
    threshold = df["FreightPerUnit"].quantile(0.75)

    df["RiskFlag"] = np.where(
        df["FreightPerUnit"] > threshold,
        1,
        0
    )

    return df


def prepare_features(df):
    features = [
        "TotalQuantity",
        "TotalPurchaseDollars",
        "AvgPurchasePrice",
        "PurchaseCostPerUnit"
    ]

    X = df[features]
    y_regression = df["Freight"]
    y_classification = df["RiskFlag"]

    return X, y_regression, y_classification