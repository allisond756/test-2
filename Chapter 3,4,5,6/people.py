people = {
    'adaniel': {
        'first':'allison',
        'last':'daniel',
        'age': '24',
        'city':'houston'
    },

    'edimaggio': {
        'first':'emma',
        'last':'dimaggio',
        'age':'25',
        'city':'redondo beach',
    },
   
}

for username, user_info in people.items():
    print("This is " + user_info['first'] + " " +
         user_info['last'] + " and they are " + user_info['age'] + 
         " years old. They live in " + user_info['city'] + ".")