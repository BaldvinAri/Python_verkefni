def get_emails():
    EXIT = "q"
    emails = []
    option = input("Email address: ")

    while option != EXIT:
        emails.append( option )
        option = input("Email address: ")

    return emails

def get_names_and_domains(emails):
    return [ tuple( i.split("@") ) for i in emails]
    

# Main program starts here - DO NOT change it

email_list = get_emails()
print(email_list)
names_and_domains = get_names_and_domains(email_list)
print(names_and_domains)