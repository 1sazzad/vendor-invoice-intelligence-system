import sqlite3
import pandas as pd
import os

DB_PATH = "data/inventory.db"
OUTPUT_PATH = "data/processed_invoice_data.csv"

os.makedirs("data", exist_ok=True)

def extract_data():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT 
        p.VendorNumber,
        p.VendorName,
        p.Brand,
        SUM(p.Quantity) AS TotalQuantity,
        SUM(p.Dollars) AS TotalPurchaseDollars,
        AVG(pp.Price) AS AvgPurchasePrice,
        AVG(vi.Freight) AS Freight
    FROM purchases p
    JOIN purchase_prices pp
        ON p.Brand = pp.Brand
    JOIN vendor_invoice vi
        ON p.PONumber = vi.PONumber
    GROUP BY 
        p.VendorNumber,
        p.VendorName,
        p.Brand
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    print("Extracted data shape:", df.shape)

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"Data saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    extract_data()