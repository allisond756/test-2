favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

friends=['amy','edward','maci','jen']

for name in favorite_languages.keys():
    if name in friends:
        print("Thank you " + name + " for taking poll")
