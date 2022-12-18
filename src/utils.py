import pandas as pd

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

#Main function for reading and processing csv file
def process_file(file_name):
    
    print("Processing transactions...",end='')
    df = pd.read_csv(file_name)
    print("Done")
    
    print("Processing transactions...",end='')
    balance = calculate_balance(df)
    avg_credit = calculate_credit(df)
    avg_debit = calculate_debit(df)
    monthly_transactions = calculate_monthly_transactions(df)
    print("Done")

    return balance, avg_credit, avg_debit, monthly_transactions
