import os
import sys
import time
import joblib
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

sys.path.append("src")

from preprocess import clean_data, feature_engineering, prepare_features


DATA_PATH = "data/processed_invoice_data.csv"
MODEL_DIR = "models"

os.makedirs(MODEL_DIR, exist_ok=True)


def evaluate_model(model_name, model, X_test, y_test):
    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)

    print(f"\nModel: {model_name}")
    print(f"MAE  : {mae:.4f}")
    print(f"RMSE : {rmse:.4f}")
    print(f"R2   : {r2:.4f}")

    return {
        "model_name": model_name,
        "model": model,
        "mae": mae,
        "rmse": rmse,
        "r2": r2
    }


def train():
    print("Loading data...")
    df = pd.read_csv(DATA_PATH)

    print("Cleaning data...")
    df = clean_data(df)

    print("Feature engineering...")
    df = feature_engineering(df)

    X, y_regression, _ = prepare_features(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y_regression,
        test_size=0.2,
        random_state=42
    )

    models = {
        "Linear Regression": LinearRegression(),

        "Decision Tree Regressor": DecisionTreeRegressor(
            max_depth=10,
            random_state=42
        ),

        "Random Forest Regressor": RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )
    }

    results = []

    for model_name, model in models.items():
        print(f"\nTraining {model_name}...")

        start_time = time.time()

        model.fit(X_train, y_train)

        end_time = time.time()
        training_time = end_time - start_time

        print(f"Training time: {training_time:.2f} seconds")

        result = evaluate_model(model_name, model, X_test, y_test)
        result["training_time"] = training_time

        results.append(result)

    best_model = max(results, key=lambda x: x["r2"])

    print("\nBest Model:")
    print(best_model["model_name"])
    print("Best R2:", best_model["r2"])

    joblib.dump(best_model["model"], f"{MODEL_DIR}/best_freight_model.pkl")
    joblib.dump(X.columns.tolist(), f"{MODEL_DIR}/feature_columns.pkl")

    print("\nBest model saved successfully.")


if __name__ == "__main__":
    train()