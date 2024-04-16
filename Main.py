def cypher(sentence, offset):
    while offset > 26:
        offset -= 26
    alphabetsoup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                    "o", "p", "q", "r", "s", "t",
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
                    "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                    "o", "p", "q", "r", "s", "t",
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
    alphabetsoup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                    "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
    sentence = sentence.casefold()
    for x in range(26):
        changing_sentence = sentence
        changing_sentence = list(changing_sentence)
        offset = x
        for p in range(len(changing_sentence)):
            if changing_sentence[p] == ' ':
                continue
            else:
                changing_sentence[p] = alphabetsoup[alphabetsoup.index(changing_sentence[p]) + offset]
        str1 = ""
        print("offset = {}, {}".format(x + 1, str1.join(changing_sentence)))


def decryptadvanced(sentence):
    alphabetsoup = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u", "v", "w", "x", "y", "z"]
    goodwords = ['the', 'be', 'to', 'of', 'and', 'in', 'that', 'have', 'it', 'for', 'not', 'on', 'with', 'he',
                 'as', 'you', 'do']
    listofsplitsentences = []
    listofnonsplitsentences = []
    str1 = ""
    printed = False
    sentence = sentence.casefold()
    for offset in range(26):
        changing_sentence = sentence
        changing_sentence = list(changing_sentence)
        for q in range(len(changing_sentence)):
            changed_amount = 0
            if changing_sentence[q] != ' ':
                while alphabetsoup.index(changing_sentence[q]) + offset >= 26:
                    offset -= 26
                    changed_amount += 1
                changing_sentence[q] = alphabetsoup[alphabetsoup.index(changing_sentence[q]) + offset]
                for u in range(changed_amount):
                    offset += 26
            print(sentence)
        str1 = ""
        listofnonsplitsentences.append("offset = {}, {}".format(offset, str1.join(changing_sentence)))
        var2 = str1.join(changing_sentence)
        var2 = var2.split()
        listofsplitsentences.append(var2)
    for r in range(len(listofsplitsentences)):
        for h in range(len(listofsplitsentences[r])):
            if listofsplitsentences[r][h] in goodwords:
                listofsplitsentences[r] = ['{} '.format(elem) for elem in listofsplitsentences[r]]
                print(str1.join(listofsplitsentences[r]))
                printed = True
    if not printed:
        for repeat in range(len(listofnonsplitsentences)):
            print(listofnonsplitsentences[repeat])


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
            yes = input("do you want to use advanced search? ")
            if yes == 'yes':
                decryptadvanced(texts)
            else:
                decrypt(texts)
    else:
        print("Unrecognised input")
