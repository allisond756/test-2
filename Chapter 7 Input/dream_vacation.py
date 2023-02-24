prompt = input("Would you like to enter our poll?")

responses = {}

polling_active = True
while polling_active:
    name = input("What is your name?")
    response = input("Where would you like to vacation?")
    responses[name] = response
    end_poll = input("Would you like to end the poll?")
    if end_poll == 'yes':
        polling_active = False
print("POLLING RESULTS")
for name,response in responses.items():
    print(name + " would like to visit " + response + ".")
