import csv
import re


# Opens the two output csv files and write the headers.
new = open('New.csv', 'w', newline='')
invalid = open('Invalid.csv', 'w', newline='')

# Opens the original csv file and reads.
with open('Data.csv', 'r') as file:
    reader = csv.reader(file)
    newwriter = csv.writer(new)
    invalidwriter = csv.writer(invalid)
    # Read the file line by line
    for i, row in enumerate(reader):
        # If not the header
        if i > 0:
            newrow = [row[0], row[3]]
            # Regex check if email is valid and write in appropriate csvs. 
            if re.match("[\w-]+@[\w-]+\.[\w-]+\.?[\w-]*", row[3]):
                newwriter.writerow(newrow)
            else:
                invalidwriter.writerow(newrow)

# Asks the user for more input
print("Input further usernames and emails. Press Control + C to stop")
while True:
    # Break if Control + C is pressed.
    try:
        # Asks for input
        username = input("Username: ")
        email = input("Email: ")
        newrow = [username, email]
        # Again, regex check if email is valid
        if re.match("[\w-]+@[\w-]+\.[\w-]+\.?[\w-]*", email):
            newwriter.writerow(newrow)
        else:
            invalidwriter.writerow(newrow)
            print("Invalid Email \"{}\", Please Try Again".format(email))
    # Break if Control + C is pressed.
    except KeyboardInterrupt:
        print("\nExiting Program, All Inputs Saved.")
        break