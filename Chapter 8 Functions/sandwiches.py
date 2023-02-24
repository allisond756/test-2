def make_sandwich(*toppings):
    print("Making a sandwich with: ")
    for topping in toppings:
        print("- " + topping)

make_sandwich('ham','cheese')
make_sandwich('mushrooms')
make_sandwich('lettuce','salami','onions','mayo')