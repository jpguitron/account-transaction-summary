from utils import process_file

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
    file_name = "data/csv/txns.csv"
    balance, avg_credit, avg_debit, monthly_transactions = process_file(file_name)
    generate_email(balance, avg_credit, avg_debit, monthly_transactions)


