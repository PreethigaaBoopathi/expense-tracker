import streamlit as st
import pandas as pd
from datetime import date

st.title("Smart Expense Tracker")

# Initialize session state
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Input section
st.subheader("Add New Expense")

amount = st.number_input("Enter Expense Amount", min_value=0.0, format="%.2f")

category = st.selectbox(
    "Category",
    ["Food", "Transport", "Shopping", "Entertainment", "Other"]
)

expense_date = st.date_input("Select Date", date.today())

# Add expense button
if st.button("Add Expense"):
    expense = {
        "Amount": amount,
        "Category": category,
        "Date": expense_date
    }
    st.session_state.expenses.append(expense)
    st.success("Expense added successfully!")

# Display expense data
st.subheader("Expense Data")

if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.dataframe(df)

    # Total expense
    total = df["Amount"].sum()
    st.subheader(f"Total Expense: ₹ {total}")

    st.subheader("Delete Individual Expense")

    # Delete option
    delete_index = st.number_input(
        "Enter row index to delete",
        min_value=0,
        max_value=len(df)-1,
        step=1
    )

    if st.button("Delete Selected Expense"):
        st.session_state.expenses.pop(delete_index)
        st.success("Expense deleted!")
        st.rerun()

    # Clear all expenses
    if st.button("Clear All Expenses"):
        st.session_state.expenses = []
        st.success("All expenses cleared!")
        st.rerun()

else:
    st.info("No expenses added yet.")
