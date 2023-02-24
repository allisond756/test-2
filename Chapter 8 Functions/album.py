def make_album(artist, title, tracks=""):
    album = {'artist name': artist, 'album title':title, 'track length': tracks}
    return album



first_album = make_album('Tame Impala','Innerspeaker',11)
print(first_album)
second_album = make_album("Beach House", "Thank Your Lucky Stars")
print(second_album)
third_album = make_album("100 gecs","1000 gecs")
print(third_album)