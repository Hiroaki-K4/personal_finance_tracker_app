import pandas as pd
from datetime import datetime

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



def view_transactions_by_date_range(df):
    while True:
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        # Validate date format
        try:
            start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")
            if start_date_dt > end_date_dt:
                print("Start date must be before or equal to end date. Please try again.")
                continue
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue

        # Filter DataFrame
        date_range = (df['Date'] >= start_date) & (df['Date'] <= end_date)
        filtered_df = df.loc[date_range]

        if not filtered_df.empty:
            print(filtered_df)
        else:
            print("There are no transactions found in this date range.")
        break

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
            print(df)

        elif option == "2":
            # 2. View Transactions by Date Range
            view_transactions_by_date_range(df)

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
            print("9. Visualize Monthly Spending Trend")
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
