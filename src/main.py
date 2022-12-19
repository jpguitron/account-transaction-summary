from utils import process_file, filter_by_client, create_required_folders
from emailmgt import generate_email
from sqlitemgt import save_txns, save_users, setup_db
import os
import pandas as pd

if __name__ == "__main__":

    txns_file = "/app/data/csv/txns.csv"
    users_file = "/app/data/csv/users.csv"
    db_file = "/app/data/db/transactions.db"
    USER_ID = os.getenv('USER_ID')

    #Get specific user information
    if USER_ID:
        print("Reading files...", end="")
        txns_df = pd.read_csv(txns_file)
        txns_df = filter_by_client(txns_df,USER_ID)
        users_df = pd.read_csv(users_file)
        users_df = filter_by_client(users_df,USER_ID)
        print("Done")

        create_required_folders()

        #Process data
        if len(users_df)>0 and len(txns_df)>0:
            balance, avg_credit, avg_debit, monthly_transactions = process_file(txns_df.copy())
            generate_email(balance, avg_credit, avg_debit, monthly_transactions)
            setup_db(db_file)
            save_txns(txns_df, db_file)
            save_users(users_df, db_file)
        else:
            print("User does not exist")
    else:
        print("User not specified")

    


