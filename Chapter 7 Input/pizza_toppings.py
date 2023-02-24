prompt = "Add as many toppings as you'd like! \n(Enter quit when finished)"

active = True
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(topping.title() + " has been added to your pizza!")