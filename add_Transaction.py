from datetime import datetime
import pandas as pd

df = pd.read_csv("sampledata.csv")

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
        if type_input in ['Expense', 'Income']:
            transaction_type = type_input
            break
        else:
            print("Invalid type! Please enter 'Expense' or 'Income'.")

    # Create a dictionary with transaction details
    new_transaction = pd.DataFrame([{
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": amount,
        "Type": transaction_type
    }])

    df = pd.concat([df, new_transaction], ignore_index=True) #Concatenates new_transaction to df as a new row
                                                                   # resetting the index to avoid duplicates.

    # print transaction details
    print(f"Date: {date}, Category: {category}, Description: {description}, Amount: {amount}, Type: {transaction_type}")
    print("Transaction added successfully!")

    df.to_csv("sampledata.csv", index=False) # Save updated DataFrame back to CSV

    return df  # Return the updated DataFrame

df = add_transaction(df) # call function collecting user inputs n appends to the original df
