prompt = "Please enter age to purchase a ticket: "

while True:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif (age > 3) and (age <= 12):
        print("Your ticket is $10.")
    elif age > 12:
        print("Your ticket is $15.")

