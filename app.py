import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Smart Expense Tracker")

amount = st.number_input("Enter Expense Amount")
category = st.selectbox("Category", ["Food","Travel","Shopping","Bills","Other"])
date = st.date_input("Select Date")

if st.button("Add Expense"):
    new_data = pd.DataFrame({
        "Amount":[amount],
        "Category":[category],
        "Date":[date]
    })

    try:
        df = pd.read_csv("expenses.csv")
        df = pd.concat([df,new_data], ignore_index=True)
    except:
        df = new_data

    df.to_csv("expenses.csv", index=False)
    st.success("Expense Added")

try:
    df = pd.read_csv("expenses.csv")

    st.subheader("Expense Data")
    st.write(df)

    st.subheader("Total Expense")
    st.write(df["Amount"].sum())

    st.subheader("Category Wise Spending")

    category_sum = df.groupby("Category")["Amount"].sum()

    fig, ax = plt.subplots()
    ax.pie(category_sum, labels=category_sum.index, autopct="%1.1f%%")

    st.pyplot(fig)

except:
    st.info("No data yet")