def cypher(sentence, offset):
    while offset > 26:
        offset -= 26
    alphabetsoup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
    realwords = ""
    sentence = sentence.casefold()
    sentence = list(sentence)
    for x in range(len(sentence)):
        if sentence[x - 1] == ' ':
            continue
        else:
            sentence[x - 1] = alphabetsoup[alphabetsoup.index(sentence[x - 1]) + offset]
    for y in range(len(sentence)):
        realwords += sentence[y - 1]
    realwords = list(realwords)
    letter = realwords.pop(0)
    realwords.append(letter)
    str1 = ""
    return str1.join(realwords)


def decryptknown(sentence, offset):
    while offset > 26:
        offset -= 26
    alphabetsoup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
    realwords = ""
    sentence = sentence.casefold()
    sentence = list(sentence)
    for x in range(len(sentence)):
        if sentence[x - 1] == ' ':
            continue
        else:
            sentence[x - 1] = alphabetsoup[alphabetsoup.index(sentence[x - 1]) - offset]
    for y in range(len(sentence)):
        realwords += sentence[y - 1]
    realwords = list(realwords)
    letter = realwords.pop(0)
    realwords.append(letter)
    str1 = ""
    return str1.join(realwords)


def decrypt(sentence):
    offset = 0
    while offset > 26:
        offset -= 26
    alphabetsoup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]

    sentence = sentence.casefold()
    sentence = list(sentence)
    listofsentences = []
    for x in range(26):
        realwords = ""
        offset = x
        for x in range(len(sentence)):
            if sentence[x - 1] == ' ':
                continue
            else:
                sentence[x - 1] = alphabetsoup[alphabetsoup.index(sentence[x - 1]) - offset]
        for y in range(len(sentence)):
            realwords += sentence[y - 1]
        realwords = list(realwords)
        letter = realwords.pop(0)
        realwords.append(letter)
        str1 = ""
        print(str1.join(realwords))
        listofsentences.append(str1.join(realwords))
    return listofsentences


while True:
    encode = input("Do you want to encode or decode? ")
    if encode == "encode":
        text = input("input sentence: ")
        off = int(input("input offset: "))
        print(cypher(text, off))
    elif encode == "decode":
        texts = input("input sentence: ")
        known = input("Do you know the offset? ")
        if known == "yes":
            off = int(input("input offset: "))
            words = decryptknown(texts, off)
            print(words)
        else:
            words = decrypt(texts)
            for x in range(26):
                print(x)
    else:
        print("Unrecognised input")

# test