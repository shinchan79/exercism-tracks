phrase = input("Enter phrase you want to check: ")
if phrase == "":
    print("Empty string! ")
else:
    list_char = list(phrase)

    c = dict((i, list_char.count(i)) for i in list_char)

    duplicate_char = []
    for char, number in c.items():
        if number >=2 and char != "-":
                duplicate_char.append(char)
    if len(duplicate_char) == 0:
        print("isogram")
    else:
        print("not isogram!")