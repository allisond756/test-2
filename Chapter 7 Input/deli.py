sandwich_orders = ['pastrami','ruben','italian','pastrami',
                   'ham and cheese','meatball sub','pastrami']
finished_sandwiches = []

print(sandwich_orders)
print("\nDeli has run out of pastrami for the day.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("Currently making your " + current_order + " sandwich.")
    finished_sandwiches.append(current_order)
print("\nCompleted orders: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
