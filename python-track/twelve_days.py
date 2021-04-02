def verse(number):
    ordinal_numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth',
                       'eleventh', 'twelfth']

    phrases = [
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, ",
        "and a Partridge in a Pear Tree."
    ]

    phrase_count = len(phrases)
    print(number)
    result = ["On the {} day of Christmas my true love gave to me: ".format(ordinal_numbers[number - 1])]
    
    if number == 1:
        result.append("a Partridge in a Pear Tree.")
    else:
        result += [phrases[index] for index in range(phrase_count - number, phrase_count)]

    return ''.join(result)


def recite(start_verse, end_verse):
    result = [verse(i) for i in range(start_verse, end_verse + 1)]

    return result