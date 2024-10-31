from datetime import datetime
import pandas as pd

df = pd.read_csv("sampledata.csv")

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
    filtered_df = df[df['Date'].str.startswith(date_input)]

    if filtered_df.empty:
        print("No transactions found for the specified date.")
        return None
    else:
        print("\nTransactions for the date:", date_input)
        for index, row in filtered_df.iterrows():
            print(f"Index: {index}, Date: {row['Date']}, Category: {row['Category']}, "
                  f"Description: {row['Description']}, Amount: {row['Amount']}, Type: {row['Type']}")

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

    description = input("Enter new description or press Enter to keep current: ").title()
    if description:
        df.at[row_index, "Description"] = description

    amount_input = input("Enter new amount or press Enter to keep current: ")
    if amount_input:
        try:
            amount = float(amount_input)
            df.at[row_index, "Amount"] = amount
        except ValueError:
            print("Invalid amount format. Keeping current amount.")

    type_input = input("Enter new type (Expense/Income) or press Enter to keep current: ").title()
    if type_input in ["Expense", "Income"]:
        df.at[row_index, "Type"] = type_input
    elif type_input:
        print("Invalid type. Keeping current type.")


    print("Transaction updated successfully!")

    return df

df = edit_transaction(df)
