import re

def validate_email(email):
    email_regex = r"[^@]+@+[^@]+\.+[^@]+"
    if re.match(email_regex, email):
        return True
    else:
        return False

# Get user input
email = input("Enter an email address: ")

# Call the function and print the result
if validate_email(email):
    print("The email address is valid.")
else:
    print("The email address is invalid.")