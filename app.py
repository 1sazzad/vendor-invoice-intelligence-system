import streamlit as st
from src.predict import predict_freight

st.set_page_config(
    page_title="Vendor Invoice Intelligence System",
    layout="centered"
)

st.title("Vendor Invoice Intelligence System")
st.write("Predict expected freight cost from vendor invoice data.")

total_quantity = st.number_input(
    "Total Quantity",
    min_value=1,
    value=100
)

total_purchase_dollars = st.number_input(
    "Total Purchase Dollars",
    min_value=1.0,
    value=1000.0
)

avg_purchase_price = st.number_input(
    "Average Purchase Price",
    min_value=0.1,
    value=10.0
)

actual_freight = st.number_input(
    "Actual Freight Cost",
    min_value=0.0,
    value=50.0
)

if st.button("Analyze Invoice"):
    predicted_freight = predict_freight(
        total_quantity,
        total_purchase_dollars,
        avg_purchase_price
    )

    difference = actual_freight - predicted_freight

    st.subheader("Result")
    st.success(f"Predicted Freight Cost: ${predicted_freight:.2f}")
    st.info(f"Actual Freight Cost: ${actual_freight:.2f}")
    st.write(f"Difference: ${difference:.2f}")

    if actual_freight > predicted_freight * 1.3:
        st.error("Status: Overcharged Invoice")

    elif actual_freight < predicted_freight * 0.7:
        st.warning("Status: Undercharged / Suspicious Invoice")

    else:
        st.success("Status: Normal Invoice")