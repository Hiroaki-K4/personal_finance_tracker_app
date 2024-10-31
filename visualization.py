import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd


def visualize_monthly_spending_trend(df):
    print("--- Visualize Monthly Spending Trend ---")
    # Get expense data, using copy to avoid affecting original df
    expense_df = df[df["Type"] == "Expense"].copy()
    # Convert Date column to datetime format
    expense_df["Date"] = pd.to_datetime(expense_df["Date"])
    # Filter month and add column called as Month
    expense_df["Month"] = expense_df["Date"].dt.to_period("M")
    # Group by Month to sum the spending
    monthly_spending = expense_df.groupby("Month")["Amount"].sum().reset_index()
    # For plotting, have to convert month back to datetime
    monthly_spending["Month"] = monthly_spending["Month"].dt.to_timestamp()

    # Line chart : Monthly Spending
    plt.plot(monthly_spending["Month"], monthly_spending["Amount"], marker="o")
    plt.title("Monthly Spending Trend")
    plt.xlabel("Month")
    plt.ylabel("Total Spending ($)")
    # Set the x-axis ticks to show only year and month
    plt.gca().xaxis.set_major_locator(
        mdates.MonthLocator()
    )  # Set major ticks to each month
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))  # Format ticks
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

    # Bar chart : Total Spending By Category
    expense_df = df[df["Type"] == "Expense"]
    total_spending = (
        expense_df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    )
    total_spending.plot(kind="bar")

    plt.title("Total Spending by Category", fontsize=16)
    plt.xlabel("Category", fontsize=14)
    plt.ylabel("Total Amount ($)", fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Pie chart : Total Spending By Category
    expense_df = df[df["Type"] == "Expense"]
    total_spending = expense_df.groupby("Category")["Amount"].sum()
    plt.pie(
        total_spending, labels=total_spending.index, autopct="%1.1f%%", startangle=140
    )
    plt.title("Percentage Distribution of Spending by Category")
    plt.axis("equal")
    plt.show()
