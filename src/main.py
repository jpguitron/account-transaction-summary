from utils import process_file
from emailmgt import generate_email

if __name__ == "__main__":
    file_name = "/app/data/csv/txns.csv"
    balance, avg_credit, avg_debit, monthly_transactions = process_file(file_name)
    generate_email(balance, avg_credit, avg_debit, monthly_transactions)


