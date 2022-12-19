import pandas as pd
import os

#Get debit average from a dataframe
def calculate_debit(df):
    return df[df['Transaction'] < 0]['Transaction'].mean()

#Get credit average from a dataframe
def calculate_credit(df):
    return df[df['Transaction'] >= 0]['Transaction'].mean()

#Get total balance
def calculate_balance(df):
    return df['Transaction'].sum()

#Get a dataframe containing a list of transactions grouped by month
def calculate_monthly_transactions(df):
    df.index = pd.to_datetime(df['Date'],format='%m/%d')

    #Lambda functions to divide data between credit and debit
    avg_debit_lambda = lambda x: x[x<0].mean()
    avg_credit_lambda = lambda x: x[x>=0].mean()

    return df.groupby(df.index.month).agg({'Transaction': [('transactions_n', 'count'), ('avg_debit', avg_debit_lambda), ('avg_credit', avg_credit_lambda)]}).reset_index()

def filter_by_client(df,USER_ID):
    return df[df['User_id'] == int(USER_ID)].reset_index()

def create_required_folders():
    email_folder = "/app/data/email"
    db_folder = "/app/data/db"

    if not os.path.exists(email_folder):
        os.makedirs(email_folder)
    if not os.path.exists(db_folder):
        os.makedirs(db_folder)

#Main function for reading and processing csv file
def process_file(df):

    print("Processing transactions...", end="")
    balance = calculate_balance(df)
    avg_credit = calculate_credit(df)
    avg_debit = calculate_debit(df)
    monthly_transactions = calculate_monthly_transactions(df)
    print("Done")

    return balance, avg_credit, avg_debit, monthly_transactions
