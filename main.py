import pandas as pd
import json

def calculate_debit(df):
    return df[df['Transaction'] < 0]['Transaction'].mean()

def calculate_credit(df):
    return df[df['Transaction'] >= 0]['Transaction'].mean()

def calculate_balance(df):
    return df['Transaction'].sum()

def calculate_monthly_transactions(df):
    transactions_df.index = pd.to_datetime(transactions_df['Date'],format='%m/%d')
    return transactions_df.groupby(transactions_df.index.month).agg({'Transaction': [('transactions_n', 'count'), ('avg_debit', lambda x: x[x<0].mean()), ('avg_credit', lambda x: x[x>=0].mean())]}).reset_index()


transactions_df = pd.read_csv("data/txns.csv")
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

balance = calculate_balance(transactions_df)
avg_credit = calculate_credit(transactions_df)
avg_debit = calculate_debit(transactions_df)
monthly_transactions = calculate_monthly_transactions(transactions_df)

print("Total balance is {}".format(balance))
print("Average credit amount: {}".format(avg_credit))
print("Average debit amount: {}".format(avg_debit))
print("Monthly results:")

for index, row in monthly_transactions.iterrows():
    print("\t{}:".format(months[int(row['Date'])-1]))
    print("\t\tNumber of transactions: {}".format(int(row['Transaction']['transactions_n'])))
    print("\t\tAverage debit amount: {}".format(row['Transaction']['avg_debit']))
    print("\t\tAverage credit amount: {}".format(row['Transaction']['avg_credit']))
