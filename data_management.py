from datetime import datetime

import pandas as pd


def import_csv_file(filename):
    return pd.read_csv(filename)


def view_transactions_by_date_range(df):
    while True:
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")

        # Validate date format
        try:
            start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_dt = datetime.strptime(end_date, "%Y-%m-%d")
            if start_date_dt > end_date_dt:
                print(
                    "Start date must be before or equal to end date. Please try again."
                )
                continue
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue

        # Filter DataFrame
        date_range = (df["Date"] >= start_date) & (df["Date"] <= end_date)
        filtered_df = df.loc[date_range]

        if not filtered_df.empty:
            print(filtered_df)
        else:
            print("There are no transactions found in this date range.")
        break


def add_transaction(df):
    while True:  # validate date
        date_input = input("Enter the date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d").date()  # def format date
            break
        except ValueError:
            print("Invalid date format! Please enter the date in YYYY-MM-DD format.")

    category = input("Enter the category (e.g., Food, Rent): ").title()
    description = input("Enter a description: ").title()

    while True:  # make sure value amount
        amount_input = input("Enter the amount: ")
        try:
            amount = float(amount_input)  # If it`s a valid float number
            break
        except ValueError:
            print("Invalid amount! Please enter a valid number.")

    while True:  # type of transaction (Expense or Income)
        type_input = input("Enter the type (Expense/Income): ").strip().title()
        if type_input in ["Expense", "Income"]:
            transaction_type = type_input
            break
        else:
            print("Invalid type! Please enter 'Expense' or 'Income'.")

    # Create a dictionary with transaction details
    new_transaction = pd.DataFrame(
        [
            {
                "Date": date,
                "Category": category,
                "Description": description,
                "Amount": amount,
                "Type": transaction_type,
            }
        ]
    )

    df = pd.concat(
        [df, new_transaction], ignore_index=True
    )  # Concatenates new_transaction to df as a new row
    # resetting the index to avoid duplicates.

    # print transaction details
    print(
        f"Date: {date}, Category: {category}, Description: {description}, Amount: {amount}, Type: {transaction_type}"
    )
    print("Transaction added successfully!")

    return df  # Return the updated DataFrame


# filtering transactions by date and bringing all indexes from the input date
def filter_transactions_by_date(df):
    while True:
        date_input = input("Enter the date to filter transactions (YYYY-MM-DD): ")
        try:
            filter_date = datetime.strptime(date_input, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format! Please enter the date in YYYY-MM-DD format.")

    # Filter the DataFrame from specific date
    # df["Date"] = df["Date"].fillna("").astype(str)
    filtered_df = df[df["Date"].str.startswith(date_input)]

    if filtered_df.empty:
        print("No transactions found for the specified date.")
        return None
    else:
        print("\nTransactions for the date:", date_input)
        for index, row in filtered_df.iterrows():
            print(
                f"Index: {index}, Date: {row['Date']}, Category: {row['Category']}, "
                f"Description: {row['Description']}, Amount: {row['Amount']}, Type: {row['Type']}"
            )

    return filtered_df


def edit_transaction(df):
    filtered_df = filter_transactions_by_date(df)
    if filtered_df is None:
        return df  # Return original df if no transaction to edit

    # Select transaction to edit
    while True:
        try:
            row_index = int(input("Enter the index of the transaction to edit: "))
            if row_index in filtered_df.index:
                break
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input! Please enter a numeric index.")

    # Displays selected transaction
    print("\nCurrent Transaction Details:")
    print(f"Date: {df.at[row_index, 'Date']}")
    print(f"Category: {df.at[row_index, 'Category']}")
    print(f"Description: {df.at[row_index, 'Description']}")
    print(f"Amount: {df.at[row_index, 'Amount']}")

    # new values values or keep the current value
    date_input = input("Enter new date (YYYY-MM-DD) or press Enter to keep current: ")
    if date_input:
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d").date()
            df.at[row_index, "Date"] = date
        except ValueError:
            print("Invalid date format. Keeping current date.")

    category = input("Enter new category or press Enter to keep current: ").title()
    if category:
        df.at[row_index, "Category"] = category

    description = input(
        "Enter new description or press Enter to keep current: "
    ).title()
    if description:
        df.at[row_index, "Description"] = description

    amount_input = input("Enter new amount or press Enter to keep current: ")
    if amount_input:
        try:
            amount = float(amount_input)
            df.at[row_index, "Amount"] = amount
        except ValueError:
            print("Invalid amount format. Keeping current amount.")

    type_input = input(
        "Enter new type (Expense/Income) or press Enter to keep current: "
    ).title()
    if type_input in ["Expense", "Income"]:
        df.at[row_index, "Type"] = type_input
    elif type_input:
        print("Invalid type. Keeping current type.")

    print("Transaction updated successfully!")

    return df


def delete_transactions(df):
    delete_idx = input("Enter the index of the transaction to delete:")
    if delete_idx.isdigit():
        delete_idx = int(delete_idx)
        if 0 <= int(delete_idx) < len(df):
            delete_df = df.drop(delete_idx).reset_index(drop=True)
            print("Transaction deleted successfully!")
            return delete_df
        else:
            print("Please enter valid input!")
            return df
    else:
        print("invalid input")
        return df


def save_transactions_to_csv(df):
    file_name = input("Enter file name to save (e.g., 'transactions.csv'): ")

    # Save dataframe as a CSV
    df.to_csv(
        file_name, index=False
    )  # index=False avoids saving the index as a column in CSV
    print(f"Transactions saved to {file_name} successfully!")
