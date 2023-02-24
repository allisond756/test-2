cities = {
    'houston':{
        'size':'big',
        'transport':'bad',
    },
    'any european city':{
        'size':'small',
        'transport':'good',
    },
}

for city, city_info in cities.items():
    print("Welcome to " + city + ". We are a " + city_info['size'] +
          " city and we have " + city_info['transport'] + 
          " transportation.")
    
print(cities.get('houston'))