import joblib
import pandas as pd

MODEL_PATH = "models/best_freight_model.pkl"
FEATURE_PATH = "models/feature_columns.pkl"

model = joblib.load(MODEL_PATH)
feature_columns = joblib.load(FEATURE_PATH)


def predict_freight(total_quantity, total_purchase_dollars, avg_purchase_price):
    purchase_cost_per_unit = total_purchase_dollars / total_quantity

    input_data = pd.DataFrame([{
        "TotalQuantity": total_quantity,
        "TotalPurchaseDollars": total_purchase_dollars,
        "AvgPurchasePrice": avg_purchase_price,
        "PurchaseCostPerUnit": purchase_cost_per_unit
    }])

    input_data = input_data[feature_columns]

    predicted_freight = model.predict(input_data)[0]

    return predicted_freight