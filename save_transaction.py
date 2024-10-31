import pandas as pd

df = pd.read_csv("sampledata.csv")


def save_transactions_to_csv(df):
    file_name = input("Enter file name to save (e.g., 'transactions.csv'): ")

    # Save dataframe as a CSV
    df.to_csv(file_name, index=False)  # index=False avoids saving the index as a column in CSV
    print(f"Transactions saved to {file_name} successfully!")

df = save_transactions_to_csv(df)