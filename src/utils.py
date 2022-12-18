import pandas as pd

def calculate_debit(df):
    return df[df['Transaction'] < 0]['Transaction'].mean()

def calculate_credit(df):
    return df[df['Transaction'] >= 0]['Transaction'].mean()

def calculate_balance(df):
    return df['Transaction'].sum()

def calculate_monthly_transactions(df):
    df.index = pd.to_datetime(df['Date'],format='%m/%d')

    avg_debit_lambda = lambda x: x[x<0].mean()
    avg_credit_lambda = lambda x: x[x>=0].mean()

    return df.groupby(df.index.month).agg({'Transaction': [('transactions_n', 'count'), ('avg_debit', avg_debit_lambda), ('avg_credit', avg_credit_lambda)]}).reset_index()

def process_file(file_name):
    df = pd.read_csv(file_name)
    
    balance = calculate_balance(df)
    avg_credit = calculate_credit(df)
    avg_debit = calculate_debit(df)
    monthly_transactions = calculate_monthly_transactions(df)

    return balance, avg_credit, avg_debit, monthly_transactions
