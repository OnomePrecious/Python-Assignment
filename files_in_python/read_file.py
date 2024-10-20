import re

var = 'yes' if re.fullmatch('labell?ed', "labelled") else "No"
print(var)

try:
    with open("account.txt", 'r') as account:
        print(account.read())
except FileNotFoundError:
    print("file not found")

