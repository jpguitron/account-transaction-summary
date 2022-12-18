def get_monthly_summary(monthly_transactions):

    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

    #Reading monthly summary template
    f = open("/app/templates/monthly_summary.html", "r")
    base = f.read()
    f.close()

    summary = ""

    #For every month of information add a new section and replace the template values
    for _, row in monthly_transactions.iterrows():
        month_summary = base.replace("<--month-->",str(months[int(row['Date'])-1]))
        month_summary = month_summary.replace("<--transactions-->",str(int(row['Transaction']['transactions_n'])))
        month_summary = month_summary.replace("<--debit-->",str(row['Transaction']['avg_debit']))
        month_summary = month_summary.replace("<--credit-->",str(row['Transaction']['avg_credit']))

        summary = summary + month_summary
    return summary

def send_email(email):
    print("Saving email...",end='')
    file = open('/app/data/email/email.html', 'w')
    file.write(email)
    file.close()
    print('done')

def generate_email(balance, avg_credit, avg_debit, monthly_transactions):
    
    print("Generating email...",end='')

    #Reading the html base template
    f = open("/app/templates/base_email.html", "r")
    base = f.read()
    f.close()

    #Replacing template values
    summary = base.replace("<--balance-->",str(balance))
    summary = summary.replace("<--credit-->",str(avg_credit))
    summary = summary.replace("<--debit-->",str(avg_debit))
    summary = summary.replace("<--monthlySummary-->",get_monthly_summary(monthly_transactions))
    print('done')

    send_email(summary)
    




