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

def generate_email(balance, avg_credit, avg_debit, monthly_transactions):
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    print("Total balance is {}".format(balance))
    print("Average credit amount: {}".format(avg_credit))
    print("Average debit amount: {}".format(avg_debit))
    print("Monthly results:")

    for index, row in monthly_transactions.iterrows():
        print("\t{}:".format(months[int(row['Date'])-1]))
        print("\t\tNumber of transactions: {}".format(int(row['Transaction']['transactions_n'])))
        print("\t\tAverage debit amount: {}".format(row['Transaction']['avg_debit']))
        print("\t\tAverage credit amount: {}".format(row['Transaction']['avg_credit']))


if __name__ == "__main__":
    file_name = "data/txns.csv"
    balance, avg_credit, avg_debit, monthly_transactions = process_file(file_name)
    generate_email(balance, avg_credit, avg_debit, monthly_transactions)


