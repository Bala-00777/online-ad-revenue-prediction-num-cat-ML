import streamlit as st
import pandas as pd
import pickle

# Load trained pipeline model
with open("model.pkl", "rb") as f:
    pipeline = pickle.load(f)

st.title("Online Advertising Revenue Prediction")

# User Inputs
month = st.selectbox("Month", ["April", "May", "June"])
day = st.number_input("Day", min_value=1, max_value=31)
campaign_number = st.selectbox("Campaign Number", ["camp 1", "camp 2", "camp 3"])
user_engagement = st.selectbox("User Engagement", ["High", "Low", "Medium"])
banner = st.selectbox("Banner Type", [
    "160 x 600", "240 x 400", "300 x 250",
    "468 x 60", "580 x 400", "670 x 90",
    "728 x 90", "800 x 250"
])
placement = st.selectbox("Placement", ["abc", "def","ghi","mno","jkl"])
displays = st.number_input("Displays")
cost = st.number_input("Cost")
clicks = st.number_input("Clicks")
post_click_conversions = st.number_input("Post Click Conversions")

# Create input dataframe
input_data = pd.DataFrame([[
    month,
    day,
    campaign_number,
    user_engagement,
    banner,
    placement,
    displays,
    cost,
    clicks,
    post_click_conversions
]], columns=[
    "month",
    "day",
    "campaign_number",
    "user_engagement",
    "banner",
    "placement",
    "displays",
    "cost",
    "clicks",
    "post_click_conversions"
])

# Prediction
if st.button("Predict Revenue"):
    prediction = pipeline.predict(input_data)

    st.success(f"Predicted Revenue: ₹{prediction[0]:,.2f}")
