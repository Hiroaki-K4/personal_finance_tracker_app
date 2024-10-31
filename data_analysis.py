import pandas as pd


def analyze_spending_by_category(df):
    print("--- Total Spending by Category ---")
    # Get expense type data
    expense_df = df[df["Type"] == "Expense"]
    # Output total spending for each category
    print(expense_df.groupby("Category")["Amount"].sum().to_string())


def calculate_average_monthly_spending(df):
    print("--- Average Monthly Spending ---")
    # Get expense type data
    expense_df = df.loc[df["Type"] == "Expense"].copy()
    # Convert Date column to datetime format
    expense_df["Date"] = pd.to_datetime(expense_df["Date"])
    # Add column called as Month
    expense_df["Month"] = expense_df["Date"].dt.to_period("M")
    # Get most recent month
    most_recent_month = expense_df["Month"].max()
    # Get most recent month's data
    recent_month_data = expense_df[expense_df["Month"] == most_recent_month]
    # Get average monthly spending(most recent month)
    average_recent_month_spending = recent_month_data["Amount"].mean()
    print(round(average_recent_month_spending, 2))


def show_top_spending_category(df):
    print("--- Top Spending Category ---")
    # Get expense data
    expense_df = df[df["Type"] == "Expense"]
    # Groupby category and get total
    totals = expense_df.groupby("Category")["Amount"].sum()
    print("{0} with {1} total spending.".format(totals.idxmax(), totals.max()))
