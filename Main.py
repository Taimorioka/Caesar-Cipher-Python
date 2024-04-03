def cypher(sentence, offset):
    while offset > 26:
        offset -= 26
    alphabetsoup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
    sentence = sentence.casefold()
    sentence = list(sentence)
    for p in range(len(sentence)):
        if sentence[p] == ' ':
            continue
        else:
            sentence[p] = alphabetsoup[alphabetsoup.index(sentence[p]) + offset]
    str1 = ""
    return str1.join(sentence)


def decryptknown(sentence, offset):
    while offset > 26:
        offset -= 26
    alphabetsoup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
    realwords = ""
    sentence = sentence.casefold()
    sentence = list(sentence)
    for p in range(len(sentence)):
        if sentence[p - 1] == ' ':
            continue
        else:
            sentence[p - 1] = alphabetsoup[alphabetsoup.index(sentence[p - 1]) - offset]
    for y in range(len(sentence)):
        realwords += sentence[y - 1]
    realwords = list(realwords)
    letter = realwords.pop(0)
    realwords.append(letter)
    str1 = ""
    return str1.join(realwords)


def decrypt(sentence):
    offset = 0
    alphabetsoup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
    sentence = sentence.casefold()
    sentence = list(sentence)
    listofsentences = []
    for l in range(26):
        realwords = ""
        offset = l
        for ex in range(len(sentence)):
            if sentence[ex] != ' ':
                sentence[ex] = alphabetsoup[alphabetsoup.index(sentence[ex]) - offset]
            else:
                continue
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
    else:
        print("Unrecognised input")
