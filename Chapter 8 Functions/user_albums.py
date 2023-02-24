def make_album(artist, title):
    album = {'artist name': artist, 'album title':title,}
    return album
while True:
    print("\nPlease input artist and album title:")
    print("(enter 'q' at any time to quit)")

    art_name = input("Artist's name: ")
    if art_name == 'q':
        break
    alb_title = input("Album's Title: ")
    if alb_title == 'q':
        break

    user_album = make_album(art_name, alb_title)
    print(alb_title + " was made by " + art_name)