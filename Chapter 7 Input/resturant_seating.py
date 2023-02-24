table = input("How many in your party tonight?")
table = int(table)
if table > 8:
    print("For a party of your size there is a 10 minute wait for the next table")
else:
    print("Right this way to your table.")