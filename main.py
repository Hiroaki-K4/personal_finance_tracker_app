import pandas as pd


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
    print(df.groupby("Category").sum()["Amount"].to_string())


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
            print("7. Calculate Average Monthly Spending")
        elif option == "8":
            # 8. Show Top Spending Category
            print("8. Show Top Spending Category")
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
