import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

st.title("Smart Expense Tracker")

# Initialize session state
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# ------------------------
# Add Expense Section
# ------------------------
st.subheader("Add New Expense")

amount = st.number_input("Enter Expense Amount", min_value=0.0, format="%.2f")

category = st.selectbox(
    "Category",
    ["Food", "Transport", "Shopping", "Entertainment", "Other"]
)

expense_date = st.date_input("Select Date", date.today())

if st.button("Add Expense"):
    expense = {
        "Amount": amount,
        "Category": category,
        "Date": expense_date
    }
    st.session_state.expenses.append(expense)
    st.success("Expense added successfully!")

# ------------------------
# Display Expense Data
# ------------------------
st.subheader("Expense Data")

if st.session_state.expenses:

    df = pd.DataFrame(st.session_state.expenses)
    st.dataframe(df)

    # Total Expense
    total = df["Amount"].sum()
    st.subheader(f"Total Expense: ₹ {total}")

    # ------------------------
    # Delete Expense
    # ------------------------
    st.subheader("Delete Individual Expense")

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

    # ------------------------
    # Clear All Expenses
    # ------------------------
    if st.button("Clear All Expenses"):
        st.session_state.expenses = []
        st.success("All expenses cleared!")
        st.rerun()

    # ------------------------
    # Pie Chart
    # ------------------------
    st.subheader("Expense Distribution (Pie Chart)")

    category_sum = df.groupby("Category")["Amount"].sum()

    fig, ax = plt.subplots()
    ax.pie(category_sum, labels=category_sum.index, autopct='%1.1f%%', startangle=90)
    ax.axis("equal")

    st.pyplot(fig)

else:
    st.info("No expenses added yet.")
