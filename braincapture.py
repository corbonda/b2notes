

# username = input("Enter username:")
# print("Username is: " + username)


def braincapture():
    while True:
        notetext = input("Text: ");
        if notetext == '':
            break;
        else:
            try:
                newnote
            except NameError:
                newnote = note(notetext)
            else:
                tmpnote = note(notetext)
                if not isinstance(newnote, list):
                    newnote = [newnote, tmpnote]
                else:
                    newnote.append(tmpnote)
    return(newnote)

note4 = braincapture()
