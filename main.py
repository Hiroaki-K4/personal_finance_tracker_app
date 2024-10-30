import pandas as pd
import matplotlib.pyplot as plt


def print_menu():
    print("=== Personal Finance Tracker ===")
    print("0. Import a CSV File")
    print("1. View All Transactions")
    print("2. View Transactions by Date Range")
    print("3. Add a Transaction")
    print("4. Edit a Transaction")
    print("5. Delete a Transaction")
    print("6. Analyze Spending by Category")
    print("7. Calculate Average Monthly Spending")
    print("8. Show Top Spending Category")
    print("9. Visualize Monthly Spending Trend")
    print("10. Save Transactions to CSV")
    print("11. Exit")


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
    plt.plot(monthly_spending["Month"], monthly_spending["Amount"] , marker='o')
    plt.title('Monthly Spending Trend')
    plt.xlabel('Month')
    plt.ylabel('Total Spending ($)')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

    # Bar chart : Total Spending By Category
    expense_df = df[df["Type"] == "Expense"]
    total_spending = expense_df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    total_spending.plot(kind='bar')

    plt.title('Total Spending by Category', fontsize=16)
    plt.xlabel('Category', fontsize=14)
    plt.ylabel('Total Amount ($)', fontsize=14)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Pie chart : Total Spending By Category
    expense_df = df[df["Type"] == "Expense"]
    total_spending = expense_df.groupby("Category")["Amount"].sum()
    plt.pie(total_spending, labels=total_spending.index, autopct='%1.1f%%', startangle=140)
    plt.title('Percentage Distribution of Spending by Category')
    plt.axis('equal')
    plt.show()


def main():
    # Import csv data
    df = pd.read_csv("sampledata.csv")

    # Application loop
    while True:
        print_menu()
        option = input("Choose an option (1-11): ")
        print()
        if option == "1":
            # 1. View All Transactions
            print("1. View All Transactions")
        elif option == "2":
            # 2. View Transactions by Date Range
            print("2. View Transactions by Date Range")
        elif option == "3":
            # 3. Add a Transaction
            print("3. Add a Transaction")
        elif option == "4":
            # 4. Edit a Transaction
            print("4. Edit a Transaction")
        elif option == "5":
            # 5. Delete a Transaction
            print("5. Delete a Transaction")
        elif option == "6":
            # 6. Analyze Spending by Category
            analyze_spending_by_category(df)
        elif option == "7":
            # 7. Calculate Average Monthly Spending
            calculate_average_monthly_spending(df)
        elif option == "8":
            # 8. Show Top Spending Category
            print("8. Show Top Spending Category")
            show_top_spending_category(df)
        elif option == "9":
            # 9. Visualize Monthly Spending Trend
            visualize_monthly_spending_trend(df)
        elif option == "10":
            # 10. Save Transactions to CSV
            print("10. Save Transactions to CSV")
        elif option == "11":
            print("Exiting the Personal Finance Tracker. Goodbye!")
            break
        else:
            print("Please enter 1-11")
            continue

        print()


if __name__ == "__main__":
    main()
