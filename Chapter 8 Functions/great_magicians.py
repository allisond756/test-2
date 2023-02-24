def show_magicians(magicians):
    """Prints magician title"""
    for magician in magicians:
        print(magician.title())

def make_great(magicians):
    """Adds The Great to magician title"""
    while magicians:
        great_magician = "The Great " + magicians.pop()
        great_magicians.append(great_magician)
    
    for great_magician in great_magicians:
        magicians.append(great_magician)
        print(magicians)
        

        

magicians = ['magical michael','hodinky','george']
great_magicians = []

make_great(magicians[:])
show_magicians(magicians)