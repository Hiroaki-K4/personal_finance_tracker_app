from data_analysis import (
    analyze_spending_by_category,
    calculate_average_monthly_spending,
    show_top_spending_category,
)
from data_management import (
    add_transaction,
    delete_transactions,
    edit_transaction,
    import_csv_file,
    save_transactions_to_csv,
    view_transactions_by_date_range,
)
from visualization import visualize_monthly_spending_trend


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


def main():
    # Import csv data
    df = import_csv_file("sampledata.csv")

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
            df = add_transaction(df)
        elif option == "4":
            # 4. Edit a Transaction
            df = edit_transaction(df)
        elif option == "5":
            # 5. Delete a Transactions
            df = delete_transactions(df)
        elif option == "6":
            # 6. Analyze Spending by Category
            analyze_spending_by_category(df)
        elif option == "7":
            # 7. Calculate Average Monthly Spending
            calculate_average_monthly_spending(df)
        elif option == "8":
            # 8. Show Top Spending Category
            show_top_spending_category(df)
        elif option == "9":
            # 9. Visualize Monthly Spending Trend
            visualize_monthly_spending_trend(df)
        elif option == "10":
            # 10. Save Transactions to CSV
            save_transactions_to_csv(df)
        elif option == "11":
            print("Exiting the Personal Finance Tracker. Goodbye!")
            break
        else:
            print("Please enter 1-11")
            continue

        print()


if __name__ == "__main__":
    main()
